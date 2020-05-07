from bs4 import BeautifulSoup
import requests
print("**********LOL  BUILDS********")
print ("type the champion :")
champ=input()
a="https://rankedboost.com/league-of-legends/build/"+champ
i=requests.get(a)
m=i.content
soup = BeautifulSoup(m, 'html.parser')
re1 = soup.findAll("div", {"class": "rb-build-spells"})[1]
z=str(re1)
soup=BeautifulSoup(z,'html.parser')
re2=soup.findAll("img",{"src":'data:image/gif;base64,R0lGODdhAQABAPAAAP///wAAACwAAAAAAQABAEACAkQBADs='})[0]
q=str(re2)
re3=soup.find("img")['title']
print("*****The runes Are ::******\n"+re3)
soup=BeautifulSoup(z,"html.parser")
re2=soup.findAll("noscript")[1]
q=str(re2)
soup=BeautifulSoup(q,'html.parser')
re2=soup.findAll("img")
q=str(re2)
re3=soup.find("img")['title']
print(re3)
soup = BeautifulSoup(m, 'html.parser')
re1 = soup.findAll("div", {"class": "rb-build-summoner-spells"})[4]
z=str(re1)
soup=BeautifulSoup(z,'html.parser')
re2=soup.findAll("img",{"src":'data:image/gif;base64,R0lGODdhAQABAPAAAP///wAAACwAAAAAAQABAEACAkQBADs='})[0]
q=str(re2)
re3=soup.find("img")['title']
print("******the build is ::******\n"+re3)
re2=soup.findAll("img",{"src":'data:image/gif;base64,R0lGODdhAQABAPAAAP///wAAACwAAAAAAQABAEACAkQBADs='})[1]
q=str(re2)
soup=BeautifulSoup(q,'html.parser')
re3=soup.find("img")['title']
print(re3)
soup=BeautifulSoup(z,"html.parser")
re3=soup.findAll("img",{"src":'data:image/gif;base64,R0lGODdhAQABAPAAAP///wAAACwAAAAAAQABAEACAkQBADs='})[2]
q=str(re3)
soup=BeautifulSoup(q,"html.parser")
re3=soup.find("img")['title']
print(re3)
soup=BeautifulSoup(z,"html.parser")
re4=soup.findAll("img",{"src":'data:image/gif;base64,R0lGODdhAQABAPAAAP///wAAACwAAAAAAQABAEACAkQBADs='})[3]
q=str(re4)
soup=BeautifulSoup(q,"html.parser")
re4=soup.find("img")['title']
print(re4)
soup=BeautifulSoup(z,"html.parser")
re5=soup.findAll("img",{"src":'data:image/gif;base64,R0lGODdhAQABAPAAAP///wAAACwAAAAAAQABAEACAkQBADs='})[4]
q=str(re5)
soup=BeautifulSoup(q,"html.parser")
re5=soup.find("img")['title']
print(re5)
soup=BeautifulSoup(z,"html.parser")
re6=soup.findAll("img",{"src":'data:image/gif;base64,R0lGODdhAQABAPAAAP///wAAACwAAAAAAQABAEACAkQBADs='})[5]
q=str(re6)
soup=BeautifulSoup(q,"html.parser")
re6=soup.find("img")['title']
print(re6)
