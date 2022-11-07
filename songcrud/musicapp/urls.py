from django.urls import path
from . import views


urlpatterns = [
    path ('', views.songlist),
    path ('artist/', views.artistlist),
    path ('lyrics/', views.lyricslist),


]
