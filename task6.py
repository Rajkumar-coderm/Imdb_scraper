from bs4 import BeautifulSoup
import requests,task,task5,os
from pprint import pprint

def movies_by_language(moviesLst):
	movie_dict={}
	for dic in moviesLst:
		for lang in dic["language"]:
			if lang not in movie_dict:
				movie_dict[lang]=1
			else:
				movie_dict[lang]+=1
	return movie_dict



movies_list=task.top250movies()
x=task5.movie_detailsLst(movies_list[:20])
pprint(movies_by_language(x))