import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
url='https://www.imdb.com/india/top-rated-indian-movies/'
res=requests.get(url)
def top250movies():
    soup=BeautifulSoup(res.text,'html.parser')
    movies=soup.find(class_='lister-list')
    onlymovies=movies.find_all(class_='titleColumn')
    name=[]
    year=[]
    link=[]
    rating=[]
    position=[]
    for movie in onlymovies:
        name.append(movie.find('a').text)
        year.append(int(movie.find(class_='secondaryInfo').text[1:5]))
        link.append('https://www.imdb.com'+movie.find('a').get('href'))
        position.append(int(movie.text.strip().split('.')[0]))
    for rate in movies.find_all(class_="ratingColumn imdbRating"):
        rating.append(float(rate.text.strip()))
    d={}
    top_250_movies=[]
    for i,j,k,l,m in zip(name,position,year,link,rating):
        d['name']=i
        d['position']=j
        d['year']=k
        d['link']=l
        d['rating']=m
        top_250_movies.append(d.copy())
    return top_250_movies
x=top250movies()

f=open('task1.json','w')
json.dump(x,f,indent=4)
# print(json.dumps(top_250_movies))
f.close()