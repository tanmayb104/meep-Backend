from . import views
from django.urls import path

urlpatterns = [
    path('league-overview', views.LeagueOverview, name="league-overview"),
    path('game-overview', views.GameOverview, name="game-overview"),
]