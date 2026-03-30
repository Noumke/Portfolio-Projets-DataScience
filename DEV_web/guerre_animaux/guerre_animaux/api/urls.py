from django.urls import path
from . import views

urlpatterns = [
    # authentification
    path('auth/login/',  views.LoginView.as_view(),  name='login'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout'),

    # armée de l'utilisateur connecté
    path('my-army/',                    views.MyArmyView.as_view(),         name='my-army'),
    path('my-army/animals/',            views.MyAnimalsView.as_view(),      name='my-animals'),
    path('my-army/animals/<int:pk>/',   views.MyAnimalDetailView.as_view(), name='my-animal-detail'),

    # gestion de l'arme d'un animal
    path('animals/<int:pk>/weapon/',    views.AnimalWeaponView.as_view(),   name='animal-weapon'),

    # vues publiques
    path('armies/',   views.PublicArmiesView.as_view(),  name='public-armies'),
    path('animals/',  views.PublicAnimalsView.as_view(), name='public-animals'),
    path('weapons/',  views.PublicWeaponsView.as_view(), name='public-weapons'),
]
