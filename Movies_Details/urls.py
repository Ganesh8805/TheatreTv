
from django.contrib import admin
from django.urls import path
from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('theatre/', views.Theatre),
    path('TV/', views.TvMovies),
]
