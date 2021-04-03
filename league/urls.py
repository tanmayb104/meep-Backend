from . import views
from django.urls import path

urlpatterns = [
    path('league-overview', views.LeagueOverview, name="league-overview"),
    path('league-list', views.leagueList, name="league-list"),
    path('league-detail/<str:pk>', views.leagueDetail, name="league-detail"),
    path('league-create', views.leagueCreate, name="league-create"),
    path('league-detail/<str:pk>/game-create/', views.gameCreate, name="game-create"),
    path('league-detail/<str:pk1>/<str:pk2>/', views.gameDetail, name="game-detail"),
    path('league-join', views.leagueJoin, name="league-join"),
    path('league-detail/<str:pk1>/<str:pk2>/game-join', views.gameJoin, name="game-join"),
]