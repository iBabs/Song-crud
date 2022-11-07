from rest_framework import serializers

from .models import Song, Artist, Lyrics

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"

class LyricSerailizer(serializers.ModelSerializer):
     class Meta:
        model = Lyrics
        fields = "__all__"