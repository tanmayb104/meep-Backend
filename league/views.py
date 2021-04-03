from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@api_view(['GET'])
def LeagueOverview(request):

    league_urls = {
        'List' : '/league-list/',
        'Detail View' : '/league-detail/<str:pk>/',
        'Create' : '/league-create/',
        'Update' : '/league-update/<str:pk>/',
        'Delete' : '/league-delete/<str:pk>/'
    }
    return Response(league_urls)

@api_view(['GET'])
def GameOverview(request):

    game_urls = {
        'List' : '/game-list/',
        'Detail View' : '/game-detail/<str:pk>/',
        'Create' : '/game-create/',
        'Update' : '/game-update/<str:pk>/',
        'Delete' : '/game-delete/<str:pk>/'
    }
    return Response(game_urls)