
from django.contrib import admin
from django.urls import path, include
from musicapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicapp.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
