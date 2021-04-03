from django.db import models
from accounts.models import User

# Create your models here.

class League(models.Model):

    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User)
    sub_users = models.ManyToManyField(User, related_name="sub_users")
    league_pic = models.ImageField(upload_to ='league_pic', null=True, blank=True)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Game(models.Model):

    name = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    league = models.ForeignKey('League',on_delete=models.CASCADE)
    bet = models.CharField(max_length=200)
    capacity = models.IntegerField()
    owner = models.ForeignKey(User)
    sub_users = models.ManyToManyField(User, related_name="sub_users")
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name