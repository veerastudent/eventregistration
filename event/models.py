from django.db import models

from django.contrib import admin
# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField
    institution = models.CharField(max_length=100)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','institution')

