from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import LeagueSerializers,GameSerializers
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string

from .models import League,Game

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def LeagueOverview(request):

    league_urls = {
        'List' : '/league-list/',
        'Create' : '/league-create/',
        'Update' : '/league-update/<str:pk>/',
        'Delete' : '/league-delete/<str:pk>/',

        'Game List' : '/league-detail/<str:pk>/',
        'Game Detail View' : '/league-detail/<str:pk>/<str:pk>/',
        'Game Create' : '/league-detail/<str:pk>/game-create/',
        'Game detail bet' : '/league-detail/<str:pk>/<str:pk>/',
        'Game Update' : '/game-update/<str:pk>/',
        'Game Delete' : '/game-delete/<str:pk>/',

        'league join' : '/league-join/',
        'game join' : ''
    }
    return Response(league_urls)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leagueList(request):
    leagues = League.objects.filter(sub_users__in=[request.user])
    serializer = LeagueSerializers(leagues, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leagueDetail(request, pk):
    league = League.objects.get(id=pk)
    games = Game.objects.filter(league=league)
    serializer = GameSerializers(games, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def leagueCreate(request):
    data = request.data
    data['code'] = get_random_string(5)
    data['owner'] = request.user.id
    data['sub_users'] = [request.user.id]
    serializer = LeagueSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        print("saved")
    else:
        print(serializer.errors)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def gameDetail(request, pk1, pk2):
    league = League.objects.get(id=pk1)
    games = Game.objects.get(league=league, id=pk2)
    serializer = GameSerializers(games, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def gameCreate(request, pk):
    data = request.data
    data['league'] = pk
    data['owner'] = request.user.id
    data['sub_players'] = [request.user.id]
    serializer = GameSerializers(data=data)
    if serializer.is_valid():
        serializer.save()
        print("saved")
    else:
        print(serializer.errors)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def leagueJoin(request):
    data = request.data
    try:
        league = League.objects.get(code=data["code"])
        league.sub_users.add(request.user.id)
        league.save()
        data = {'league-list': reverse('league-list', request=request)}
        return Response(data)

    except:
        return Response("Invalid Code")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def leagueJoin(request):
    data = request.data
    try:
        league = League.objects.get(code=data["code"])
        league.sub_users.add(request.user.id)
        league.save()
        data = {'league-list': reverse('league-list', request=request)}
        return Response(data)

    except:
        return Response("Invalid Code")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def gameJoin(request,pk1,pk2):
    league = League.objects.get(id=pk1)
    game = Game.objects.get(league=league, id=pk2)
    game.sub_players.add(request.user.id)
    game.save()
    data = {'league-detail/<str:pk1>/<str:pk2>/': reverse('gameDetail', args=[pk1, pk2], request=request)}
    return Response(data)
