from django.shortcuts import render
from .models import Theatre_Movie,TV_Movies
from django.http import HttpResponse
import requests
import pandas as pd
import json
# Create your views here.
def Theatre(request):
    #load data by request method
    response = requests.get('http://data.tmsapi.com/v1.1/movies/showings?startDate=2020-10-26&zip=78701&api_key=6hcuwjrw3trksf8ctst8yhev')
    json_responce=response.json() # convert into json
    a=[i for i in json_responce]
    #create Dataframe to manipulate data
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
    nam=name()
    j=1
    while j<15:
        theatremovie=Theatre_Movie()
        title=next(aa)
        release=next(bb)
        genre=next(cc)
        Desc=next(dd)
        theatre=next(nam)
        #Apply data to database wrt to column name nd values
        theatremovie.Title=title
        theatremovie.Release_year=release
        theatremovie.Description=Desc
        theatremovie.Genres=genre
        theatremovie.Theatre=theatre
        theatremovie.save() 
        if j==15:
            break
        j+=1
    return HttpResponse('<h1>Successful Theatre data</h1>')
    
        
def TvMovies(request):
    #load data to responce
    response = requests.get('http://data.tmsapi.com/v1.1/movies/airings?lineupId=USA-TX42500-X&startDateTime=2020-10-26T04:08&api_key=6fkm6jk424cthumtf92gs52p')
    json_responce=response.json() #convert into json
    df=pd.DataFrame(json_responce)# create dataframe of responce
    new_data=[i for i in df['program']] #fetching data from dataframe
    df2=pd.DataFrame(new_data)
    # df1=df2[['title','releaseYear','genres','shortDescription']]
    #Converting each column to Generator to fetch each time
    aa=(i for i in df2['title'])
    bb=(i for i in df2['releaseYear'])
    cc=(i for i in df2['genres'])
    dd=(i for i in df2['shortDescription'])
    qq=(i for i in df['channels'])
    j=1
    while j<400:
        TVmovie=TV_Movies()
        title=next(aa)
        release=next(bb)
        genre=next(cc)
        Desc=next(dd)
        channl=next(qq)
        #Apply data to database wrt to column name nd values
        TVmovie.Title=title
        TVmovie.Release_year=release
        TVmovie.Description=Desc
        TVmovie.Genres=genre
        TVmovie.Channel=channl
        TVmovie.save() 
        if j==378:
            break
        j+=1
    return HttpResponse('<h1>Successful TV data</h1>')