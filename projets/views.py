from django.shortcuts import render
# from django.http import HttpResponse
from . models import Projets

def index(request):

    projet=Projets.objects.all()
    return render(request,'index.html',{'projet':projet})
