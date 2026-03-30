from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Army, Animal, Weapon


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username']


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Weapon
        fields = ['id', 'name', 'damage', 'description']


class AnimalSerializer(serializers.ModelSerializer):
    #Lecture imbriquée de l'arme avec ses détails
    weapon = WeaponSerializer(read_only=True)

    #Champ d'écriture pour assigner une arme existante par son ID
    weapon_id = serializers.PrimaryKeyRelatedField(
        queryset=Weapon.objects.all(),
        source='weapon',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model  = Animal
        fields = ['id', 'name', 'breed', 'image_url', 'army', 'weapon', 'weapon_id']
        #L'armée est assignée automatiquement via la vue, pas par l'utilisateur
        read_only_fields = ['army']


class ArmySerializer(serializers.ModelSerializer):
    owner        = UserSerializer(read_only=True)           #Propriétaire en lecture seule
    animals      = AnimalSerializer(many=True, read_only=True)  #Liste des animaux
    animal_count = serializers.ReadOnlyField()              #Propriété calculée

    class Meta:
        model  = Army
        fields = ['id', 'name', 'description', 'owner', 'animal_count', 'animals', 'created_at']
