from django.db import models
from django.contrib.auth.models import User

class Expansion(models.Model):
    expansion_name = models.CharField(max_length=100, unique=True)
    expansion_img = models.ImageField(upload_to='expansion_images/', default='expansion_images/blank.jpg')
    expansion_amount = models.IntegerField()

    def __str__(self):
        return self.expansion_name

class Card(models.Model):
    card_name = models.CharField(max_length=100)
    expansion_name = models.ForeignKey(Expansion, on_delete=models.CASCADE)
    card_number = models.IntegerField()
    card_img = models.ImageField(upload_to='card_images/')
    owned_by_users = models.ManyToManyField(User, blank=True, related_name='owned_cards')

    def __str__(self):
        return self.card_name