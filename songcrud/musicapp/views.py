from django.shortcuts import render
from django.http import JsonResponse
from .serializer import SongSerializer, ArtistSerializer, LyricSerailizer
from .models import Song, Artist, Lyrics
 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class= SongSerializer


@api_view(["GET","POST", "DELETE"])
def songlist(request):
    if request.method == "GET":
        songs= Song.objects.all()
        serializer = SongSerializer(songs, many =True)
        return Response({"Songs":serializer.data})
    
    if request.method == "POST":
        serializer= SongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


    return Response(songs)

@api_view(["GET", "POST"])
def artistlist(request):
    if request.method == "GET":
        artists= Artist.objects.all()
        serializer = ArtistSerializer(artists, many =True)
        return Response({"Artist":serializer.data})
    
    if request.method == "POST":
        serializer= ArtistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(artists)

@api_view(["GET", "POST"])
def lyricslist(request):
    if request.method == "GET":
        lyrics= Lyrics.objects.all()
        serializer = LyricSerailizer(lyrics, many =True)
        return Response({"Lyrics":serializer.data})
    
    if request.method == "POST":
        serializer= LyricSerailizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(lyrics)