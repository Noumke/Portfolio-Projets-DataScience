from django.contrib import admin
from .models import Army, Animal, Weapon

#Enregistrement des modèles dans l'interface d'administration Django
admin.site.register(Weapon)
admin.site.register(Army)
admin.site.register(Animal)
