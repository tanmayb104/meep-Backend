from . import views
from django.urls import path

urlpatterns = [
    path('league-overview', views.LeagueOverview, name="league-overview"),
    path('league-list', views.leagueList, name="league-list"),
    path('league-detail/<str:pk>', views.leagueDetail, name="league-detail"),
    path('league-create', views.leagueCreate, name="league-create"),
]