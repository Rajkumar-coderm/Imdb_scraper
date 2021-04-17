import json,task,task8#task5,task8
from pprint import pprint

def movies_byDirector_language(movie_detailsLst):
	mainDic={}
	for dic in movie_detailsLst:
		subdic={}
		for direc in dic["director"]:
			if direc not in mainDic:
				mainDic[direc]=subdic.copy()
		
				for dic in movie_detailsLst:
					for director in dic["director"]:
						if director ==direc:
							for lang in dic["language"]:
								if lang not in mainDic[direc]:
									mainDic[direc][lang]=1
								else:
									mainDic[direc][lang]+=1
	return mainDic
movies_list=task.top250movies()
x=task8.movie_detailsLst(movies_list)
v=movies_byDirector_language(x)
op=open("task10.json","w")
op.write(json.dumps(v,indent=4))
op.close()
# pprint(movies_byDirector_language(x))
