from django.shortcuts import render
from django.http import JsonResponse
from .serializer import SongSerializer
from .models import Song
 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class= SongSerializer


@api_view(["GET","POST"])
def songlist(request):
    if request.method == "GET":
        songs= Song.objects.all()
        serializer = SongSerializer(songs, many =True)
        return JsonResponse({"Songs":serializer.data})
    
    if request.method == "POST":
        serializer= SongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)


