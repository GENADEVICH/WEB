from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def addfile (request):
    return render(request, 'main/addfile.html')

def album (request):
    return render(request, 'main/album.html')
def avtoriz (request):
    return render(request, 'main/avtoriz.html')

def music (request):
    return render(request, 'main/music.html')

def performers (request):
    return render(request, 'main/performers.html')

def playlist (request):
    return render(request, 'main/playlist.html')

def podcast (request):
    return render(request, 'main/podcast.html')

def profile (request):
    return render(request, 'main/profile.html')

def radio (request):
    return render(request, 'main/radio.html')
def register (request):
    return render(request, 'main/register.html')

def settings (request):
    return render(request, 'main/settings.html')