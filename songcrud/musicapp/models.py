from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name= models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    age = models.IntegerField()

    def __str__(self):
        return  (self.first_name)


class Song(models.Model):
    title = models.CharField(max_length = 25)
    artist_id = models.ForeignKey(Artist, on_delete = models.CASCADE)
    date_released = models.DateTimeField
    likes = models.IntegerField

    def __str__(self):
        return  (self.title)

class Lyrics(models.Model):
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return  (self.content)



