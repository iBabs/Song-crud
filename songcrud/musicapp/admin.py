from django.contrib import admin
from .models import Artist, Song, Lyrics

# Register your models here.



admin.site.register(Lyrics)

@admin.register(Artist)
class  ArtistAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'age', )

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('artist_id', 'date_released')