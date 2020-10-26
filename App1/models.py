from django.db import models

# Create your models here.
class Theatre_Movie(models.Model):
    Title=models.CharField(max_length=100)
    Release_year=models.CharField(max_length=30)
    Genres=models.CharField(max_length=200)
    Description=models.CharField(max_length=500)
    Theatre=models.CharField(max_length=300)
    def __str__(self):
        return self.Title
        
class TV_Movies(models.Model):
    Title=models.CharField(max_length=100)
    Release_year=models.CharField(max_length=30)
    Genres=models.CharField(max_length=200)
    Description=models.CharField(max_length=500)
    Channel=models.CharField(max_length=300)

    def __str__(self):
        return self.Title