from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import SearchUser


def inici(request):
    voidSearchUser = SearchUser()
    if request.method == "POST":
        name1=request.POST.get('name1', '')
        name2=request.POST.get('name2', '')
        try:
            user1 = User.objects.get(username=name1)

        except User.DoesNotExist as e:
            user1="No trobat"
        try:
            user2 = User.objects.get(username=name2)
        except User.DoesNotExist as e:
            user2="No trobat"
        context = {
            'user1':user1,
            'user2':user2,
        }
        return render(request,'crawler/information.html', context)
    return render(request,'crawler/inici.html', {'SearchUser':voidSearchUser})
def information(request):
    return render(request,'crawler/information.html')
# Create your views here.
