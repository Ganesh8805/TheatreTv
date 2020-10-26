import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Movies_Details.settings')
import django
django.setup()
from App1.models import Theatre_Movie
import requests
import pandas as pd


response = requests.get('http://data.tmsapi.com/v1.1/movies/showings?startDate=2020-10-26&zip=78701&api_key=6hcuwjrw3trksf8ctst8yhev')
json_responce=response.json()
a=[i for i in json_responce]
df=pd.DataFrame(a)
df1=df[['title','releaseYear','genres','shortDescription',]]
aa=(i for i in df1['title'])
bb=(i for i in df1['releaseYear'])
cc=(i for i in df1['genres'])
dd=(i for i in df1['shortDescription'])
qq=[i for i in df['showtimes']]
def name():
    for i in qq:
        for j in i:
            yield( j['theatre']['name'])
name()  
j=1
while j<20:
    title=next(aa)
    release=next(bb)
    genre=next(cc)
    Desc=next(dd)
    theatre=next(name())
    Theatre_Detail=Theatre_Movie.objects.create(Title=title,Release_year=release,
        Genres=genre,Description=Desc,Theatre=theatre)    
    # Theatre_Movie().save()
    if j==14:
        break
    j+=1