from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SearchUser


def inici(request):
    voidSearchUser = SearchUser()
    if request.method == "POST":
        name1=request.POST.get('name1', '')
        name2=request.POST.get('name2', '')

    return render(request,'crawler/inici.html', {'SearchUser':voidSearchUser})
