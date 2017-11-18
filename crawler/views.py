import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Photos
from .forms import SearchUser


def inici(request):
    voidSearchUser = SearchUser()
    if request.method == "POST":
        name1=request.POST.get('name1', '')
        name2=request.POST.get('name2', '')
        try:
            user1 = User.objects.get(username=name1)
        except User.DoesNotExist:
            user1 = None
        try:
            user2 = User.objects.get(username=name2)
        except User.DoesNotExist:
            user2 = None

        context = {
            'user1': user1,
            'user1_wc': get_wordcloud(user1) if user1 else [],
            'user2': user2,
            'user2_wc': get_wordcloud(user2) if user2 else [],
        }
        return render(request,'crawler/information.html', context)
    return render(request,'crawler/inici.html', {'SearchUser':voidSearchUser})


def get_wordcloud(user):
    # TODO: get from one query instead
    wordcloud = {}
    for photo in Photos.objects.filter(owner=user).all():
        for tag in photo.hashtags.split(','):
            t = tag.strip()[1:]
            wordcloud[t] = wordcloud.setdefault(t, 0) + 1
    return [[k, wordcloud[k]] for k in wordcloud]

def information(request):
    return render(request,'crawler/information.html')
