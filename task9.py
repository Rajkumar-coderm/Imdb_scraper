import os,json,requests,time,random,task
from bs4 import BeautifulSoup
from pprint import pprint

def movie_detailsLst(movies):
	movie_details_list=[]
	for movie in movies:
		link0=movie["link"]
		if os.path.exists("/home/navgurukul/Documents/"+link0[-10:-1]+".json"):
			print("Bhai file mil gyi:")
			with open("/home/navgurukul/Documents/"+link0[-10:-1]+".json") as file:
				movie_details_list.append(json.loads(file.read()))
		else:
			import time
			print("please wait a five second i am searching ")
			time.sleep(random.randint(1,3))
			page=requests.get(link0).text

			genre_lst=[]
			director_lst=[]

			data=BeautifulSoup(page,"html.parser")
			name=data.find(class_="title_wrapper").h1.text
			timeClass=data.find(class_="title_wrapper")
			time=(timeClass.find(class_="subtext").time.text).strip()
			genre_class=timeClass.find(class_="subtext")
			genre_a=genre_class.find_all("a")
			for i in range(len(genre_a)-1):
				genre_lst.append(genre_a[i].text)

			bio=data.find(class_="summary_text").text
			director_class=data.find(class_="credit_summary_item")
			director_a=director_class.find_all("a")
			for i in range(len(director_a)):
				director_lst.append(director_a[i].text)
			link=data.find(class_="poster").img["src"]
			exta_details=data.find("div",attrs={"class":"article","id":"titleDetails"})
			txt_div=exta_details.find_all("div",class_="txt-block")
			count=0
			for div in txt_div:
				if count==2:
					break

				elif div.h4.text== "Country:":
					country_all= div.find_all("a")
					country=[a.text for a in country_all]
					count+=1
				elif div.h4.text=="Language:":
					language_all=div.find_all("a")
					language=[a.text for a in language_all]
					count+=1

			s={}
			s["name"]=name[:-8]
			s["country"]="india"
			s["genre"]=genre_lst
			if len(time)==2:
				s["running_time"]=int(time[0])*60
			else:
				s["running_time"]=int(time[0])*60+int(time[3])
			s["minfo"]=bio.strip()
			s["director"]=director_lst
			s["poster_link"]=link
			s["language"]=language
			s["country"]=country
			movie_details_list.append(json.dumps(s))
			with open("/home/navgurukul/Documents/"+link0[-10:-1]+".json","w") as file:
				file.write(json.dumps(s,indent=4))
	return movie_details_list	
moviesLst=task.top250movies()
pprint(movie_detailsLst(moviesLst))