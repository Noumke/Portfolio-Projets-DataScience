from django.db import models
from django.contrib.auth.models import User


# modèle pour les armes
class Weapon(models.Model):
    name        = models.CharField(max_length=100)
    damage      = models.IntegerField(default=0)      # points de dégâts
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.damage} dégâts)"


# modèle pour les armées (une armée par utilisateur)
class Army(models.Model):
    owner       = models.OneToOneField(User, on_delete=models.CASCADE, related_name='army')
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} [{self.owner.username}]"

    @property
    def animal_count(self):
        # nombre d'animaux calculé dynamiquement
        return self.animals.count()


# modèle pour les animaux (chaque animal appartient à une armée)
class Animal(models.Model):
    name      = models.CharField(max_length=100)
    breed     = models.CharField(max_length=100, blank=True)    # race de l'animal
    image_url = models.URLField(blank=True)
    army      = models.ForeignKey(Army, on_delete=models.CASCADE, related_name='animals')
    weapon    = models.ForeignKey(
        Weapon, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='animals'
    )

    def __str__(self):
        return f"{self.name} ({self.breed}) — armée: {self.army.name}"
