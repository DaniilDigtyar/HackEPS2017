from django.shortcuts import render
from .models import Users
def inici(request):
    nom_usuari=Users.user
    return render(request,'crawler/inici.html',{'nom_usuari':nom_usuari})

# Create your views here.
