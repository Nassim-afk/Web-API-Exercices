#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:19:01 2019

@author: nassim
"""

import requests
from bs4 import BeautifulSoup

#1.1 Affichage des noms et numéros de téléphone de l'équipe du lip6

r = requests.get("https://www.lip6.fr/recherche/team_membres.php?acronyme=NPA")
soup = BeautifulSoup(r.content, "html.parser")
pars=soup.find_all('tr')
for i in pars :
    name=i.find('a',attrs={"class": not ("nouser")})
    tel=i.find('td',attrs={"class":"tel"})
    print(name.string,tel.string)
    
print("********************************")    
#2.1 affichage de tout les pays
"""
a= requests.get("https://fr.wikipedia.org/wiki/Liste_des_pays_par_densit%C3%A9_de_population")
b = BeautifulSoup(a.content, "html.parser")
c=b.find_all('tr')
for j in c :
    
    tel2=j.find('span',attrs={"class":"datasortkey"})
    print(tel2.string)
 """
w=requests.get("https://fr.wikipedia.org/wiki/Liste_des_pays_par_densit%C3%A9_de_population")
L = BeautifulSoup(w.content, "html.parser")

pays=L.find_all('span',attrs={"class": "datasortkey"})
for div in pays:
     print(div.text)  

     
G=L.find_all('td')
dico={}
x=[]
y=[]
z=[]
v=[]
w=[]

for i in range(199):
    a=G[i+(4*i)].string
    x.append(a)
    b=G[i+1+(4*i)].text
    y.append(b)
    c=G[i+2+(4*i)].string
    z.append(c)
    d=G[i+3+(4*i)].string
    w.append(d)
    e=G[i+4+(4*i)].string
    v.append(e)

for i in range(len(x)):
    print('rang :',x[i])
    print('pays :',y[i])
    print('densité (hab/km) :',z[i])
    print('population (hab) :',w[i])
    print('superficie (km²) :',v[i])
    
dico['rang']=list(x)
dico['pays']=list(y)
dico['densité']=list(z)
dico['poplation']=list(w)
dico['superficie']=list(v)


#la densité d'un pays
pay=input('Le nom du pays dont vous voulez la densité :')
pay_dico=dico.get('pays')
x='\xa0'+pay
jdx=0
idx=0
for i in range(len(pay_dico)):
    jdx=jdx+1
    if pay_dico[i]==x:
        idx=jdx
    

#Savoir quel est le pays au rang x, donner x
print('la densité de',pay,'est : ',dico.get('densité')[idx-1],'hab/km²') 
 
rang=input('le rang : ')

# il y a 4 pays qui n'ont pas de rang donc on ajoute ces 4 conditions
rang=int(rang)
if rang<69:
    u=int(rang)-1
if 69<= rang <129:
    u=int(rang)
if 129<= rang <150:
    u=int(rang)+1
if 150<= rang <173:
    u=int(rang)+2
if 173<= rang <196:
    u=int(rang)+3

print('le pays avec le rang',rang,'est :',dico.get('pays')[u])   
