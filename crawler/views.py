from django.shortcuts import render
from .forms import SearchUser
from django.http import HttpResponse, HttpResponseRedirect
def inici(request):
    voidSearchUser = SearchUser()
    if request.method == "POST":
        name=request.POST.get('name', '')
    return render(request,'crawler/inici.html', {'SearchUser':voidSearchUser})


# Create your views here.
