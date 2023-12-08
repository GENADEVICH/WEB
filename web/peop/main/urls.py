from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('', views.register, name='register'),
    path('index', views.index, name='index'),
    path('addfile', views.addfile, name='addfile'),
    path('album', views.album, name='album'),
    path('avtoriz', views.avtoriz, name='avtoriz'),
    path('music', views.music, name='music'),
    path('performers', views.performers, name='performers'),
    path('playlist', views.playlist, name='playlist'),
    path('podcast', views.podcast, name='podcast'),
    path('profile', views.profile, name='profile'),
    path('radio', views.radio, name='radio'),
    path('settings', views.settings, name='settings'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
