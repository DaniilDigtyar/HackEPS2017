from django.shortcuts import render
from .forms import SearchUser
from django.http import HttpResponse, HttpResponseRedirect

def inici(request):
    voidSearchUser = SearchUser()
    if request.method == "POST":
        name1=request.POST.get('name1', '')
        name2=request.POST.get('name2', '')
        print name1
        print name2

    return render(request,'crawler/inici.html', {'SearchUser':voidSearchUser})


# Create your views here.
