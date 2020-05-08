from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
url = "https://socialblade.com/youtube/"

headers = {"User-Agent": "Mozilla/5.0","Referer":"http://www.google.com"}
req=Request(url,headers=headers)
s=urlopen(req).read()
soup = BeautifulSoup(s.decode(),"lxml")

a=soup.findAll("div",{"class":"table-body"})
print("name", "grade" , "rank", "videos" , "subscriber", "views")
for i in a:
	rank=i.find("div",{"class":"section-rank"}).text
	grade = i.find("span").text
	name = i.find("a").text
	b=i.findAll("div",{"class":"section-lg"})
	videos=b[0].text
	subscriber = b[1].text
	views = b[2].text
	print(name, grade , rank, videos , subscriber, views)
	print("")