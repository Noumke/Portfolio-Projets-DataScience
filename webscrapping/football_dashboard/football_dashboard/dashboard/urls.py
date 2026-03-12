from django.urls import path
from . import views

urlpatterns = [
    path('',                     views.home,            name='home'),
    path('ligue/<str:nom_ligue>/', views.ligue,          name='ligue'),
    path('joueurs/',              views.joueurs,         name='joueurs'),
    path('equipes/',              views.equipes,         name='equipes'),
    path('matchs/',               views.matchs,          name='matchs'),
    path('api/buts-journee/',     views.api_buts_journee, name='api_buts'),
    path('api/forme-equipe/',     views.api_forme_equipe, name='api_forme'),
]
