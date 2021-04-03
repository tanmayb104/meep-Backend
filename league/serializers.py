from rest_framework import serializers
from .models import League,Game

class LeagueSerializers(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'