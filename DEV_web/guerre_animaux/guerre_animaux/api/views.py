from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from .models import Army, Animal, Weapon
from .serializers import ArmySerializer, AnimalSerializer, WeaponSerializer, UserSerializer


# AUTHENTIFICATION

class LoginView(APIView):
    # connexion : retourne un token d'authentification
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # on vérifie les identifiants
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Identifiants invalides.'}, status=400)

        # on crée ou récupère le token de l'utilisateur
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data
        })


class LogoutView(APIView):
    # déconnexion : supprime le token de l'utilisateur
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # on supprime le token pour invalider la session
        request.user.auth_token.delete()
        return Response({'message': 'Déconnecté avec succès.'})


# GESTION DE L'ARMEE DE L'UTILISATEUR CONNECTE

class MyArmyView(APIView):
    # CRUD sur l'armée de l'utilisateur authentifié
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # on récupère l'armée de l'utilisateur
        try:
            army = request.user.army
        except Army.DoesNotExist:
            return Response({'detail': "Vous n'avez pas encore d'armée."}, status=404)
        return Response(ArmySerializer(army).data)

    def post(self, request):
        # création de l'armée (une seule par utilisateur)
        if hasattr(request.user, 'army'):
            return Response({'error': 'Vous avez déjà une armée.'}, status=400)
        serializer = ArmySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        # modification du nom ou de la description
        try:
            army = request.user.army
        except Army.DoesNotExist:
            return Response({'error': "Aucune armée à modifier."}, status=404)
        serializer = ArmySerializer(army, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


# GESTION DES ANIMAUX DE L'ARMEE

class MyAnimalsView(APIView):
    # liste et ajout d'animaux dans l'armée de l'utilisateur
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # on récupère tous les animaux de l'armée
        try:
            animals = request.user.army.animals.all()
        except Army.DoesNotExist:
            return Response([], status=200)
        return Response(AnimalSerializer(animals, many=True).data)

    def post(self, request):
        # ajout d'un animal à l'armée
        try:
            army = request.user.army
        except Army.DoesNotExist:
            return Response({'error': "Créez d'abord une armée."}, status=400)
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(army=army)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class MyAnimalDetailView(APIView):
    # suppression d'un animal de l'armée
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        # on vérifie que l'animal appartient bien à l'armée de l'utilisateur
        try:
            animal = request.user.army.animals.get(pk=pk)
        except (Army.DoesNotExist, Animal.DoesNotExist):
            return Response({'error': "Animal introuvable dans votre armée."}, status=404)
        animal.delete()
        return Response(status=204)


# GESTION DE L'ARME D'UN ANIMAL

class AnimalWeaponView(APIView):
    # assigner ou retirer l'arme d'un animal (propriétaire uniquement)
    permission_classes = [IsAuthenticated]

    def _get_own_animal(self, request, pk):
        # on vérifie que l'animal appartient à l'armée de l'utilisateur
        try:
            return request.user.army.animals.get(pk=pk)
        except (Army.DoesNotExist, Animal.DoesNotExist):
            return None

    def post(self, request, pk):
        # assigner une arme existante (weapon_id) ou en créer une nouvelle
        animal = self._get_own_animal(request, pk)
        if not animal:
            return Response({'error': "Animal introuvable ou non autorisé."}, status=403)

        weapon_id = request.data.get('weapon_id')
        if weapon_id:
            # on assigne une arme existante par son ID
            weapon = get_object_or_404(Weapon, pk=weapon_id)
            animal.weapon = weapon
            animal.save()
        else:
            # on crée une nouvelle arme et on l'assigne
            w_serializer = WeaponSerializer(data=request.data)
            if w_serializer.is_valid():
                weapon = w_serializer.save()
                animal.weapon = weapon
                animal.save()
            else:
                return Response(w_serializer.errors, status=400)

        return Response(AnimalSerializer(animal).data)

    def delete(self, request, pk):
        # on retire l'arme de l'animal sans la supprimer
        animal = self._get_own_animal(request, pk)
        if not animal:
            return Response({'error': "Non autorisé."}, status=403)
        animal.weapon = None
        animal.save()
        return Response(status=204)


# VUES PUBLIQUES (accessibles sans authentification)

class PublicArmiesView(APIView):
    # liste publique de toutes les armées
    permission_classes = [AllowAny]

    def get(self, request):
        armies = Army.objects.all().select_related('owner').prefetch_related('animals__weapon')
        return Response(ArmySerializer(armies, many=True).data)


class PublicAnimalsView(APIView):
    # liste publique de tous les animaux
    permission_classes = [AllowAny]

    def get(self, request):
        animals = Animal.objects.all().select_related('weapon', 'army__owner')
        return Response(AnimalSerializer(animals, many=True).data)


class PublicWeaponsView(APIView):
    # liste publique des armes, création réservée aux connectés
    permission_classes = [AllowAny]

    def get(self, request):
        # accessible à tout le monde
        weapons = Weapon.objects.all()
        return Response(WeaponSerializer(weapons, many=True).data)

    def post(self, request):
        # création d'une arme réservée aux utilisateurs authentifiés
        if not request.user.is_authenticated:
            return Response({'error': 'Authentification requise.'}, status=401)
        serializer = WeaponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
