from task5 import movie_detailsLst
def movies_by_director(movie_detailsLst):
    movie_dict={}
    for dic in movie_detailsLst:
        for direc in dic["director"]:
            if direc not in movie_dict:
                movie_dict[direc]=1
            else:
                movie_dict[direc]+=1
    op=open("task7.json","w")
    op.write(json.dumps(movie_dict,indent=4))
    op.close()
    return movie_dict
# movies_list=task.top250movies()
# x=task5.movie_detailsLst(movies_list[:10])
# print(movies_by_director(x))