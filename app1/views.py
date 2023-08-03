from django.shortcuts import render
from app1.models import *
from django.views.generic import ListView
# Create your views here.
class Trainerdata(ListView):
    model=Trainer
    template_name='Trainerdata.html'
    context_object_name='td'
    #queryset=Trainer.objects.filter(trainer_name='balaji')
    ordering=['trainer_name']