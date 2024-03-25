from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "JeuxVideos/index.html",  {

    })


def show(request, titre):
    return render(request, "JeuxVideos/show.html", {
        "nom" : titre
    })


def create(request):
    return render(request, "JeuxVideos/create.html", {

    })

def create(request):
    return render(request, "JeuxVideos/about.html", {

    })

from JeuxVideos.models import Jeux

def index(request):
    return render(request, "JeuxVideos/index.html",{})

def show(request, jeux_id):
    listeJeux = Jeux.obeject.get(jeuxID = jeux_id)
    premierJeux = listeJeux
    
    return render(request, "JeuxVideos/show.html",{
        "titre" : premierJeux.title,
        "publication": premierJeux.release,
        "content": premierJeux.content,
        "nextID": anime_id + 1,
    })
 
def create(request, userID):
    return render(request, "JeuxVideos/index.html", {
        "username" : user["username"]

    })
