#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:00:41 2019

@author: nassim
"""

import json
import requests
import folium
import webbrowser
import bottle
from html.entities import codepoint2name
from bottle import Bottle, run, static_file

decoded=json.load(open('tournagesdefilmsparis2011.json'))
a,b,c=[],[],[]
for i in decoded:   #entrer dans ce que je décode
    info=i['fields']   # m'interesse qu'à la section fields
    a.append(info.get('titre'))
    b.append(info.get('xy'))
    c.append(info.get('adresse'))
    
         # faire une liste de tout les films (sans répitition)      
title=list(a) 
title_list=[]
for i in title:
    title_list.append(i)
    t=title.count(i)
    
    for j in range(t-1):
        title.remove(i)
        
#l'association des adresses et les cordonnées à chaque film
coord=[]
adresse=[] #initialisation vide
for i in title_list :
    f=[]
    g=[]
    
    for j in range (len(b)):
        if i == a[j]: #si le titre coincide 
            f.append(b[j]) #coord
            g.append(c[j]) #adresse
    coord.append(tuple(f))
    adresse.append(tuple(g)) 
    
#Création du dictionnaire
dico={}
for i in range(len(title_list)):
    dico[title_list[i]]=(coord[i],adresse[i])
   
#création du server
@bottle.route("/qui")
@bottle.view("page.tpl")
def qui() :
    stri = "<form method='post' action='film'><SELECT name = film>"
    for i in range(len(title_list)) :
        stri += "<option>" + title_list[i] + "</option>"
    stri+= "</SELECT><hr/><input type='submit' value='confirmer'/></FORM>"""
    return {"title":"choisi un film :", "body" : stri}

@bottle.route("/film", method='POST')
@bottle.view("page.tpl")

#création de la carte et lindication des adresses de tournnage sur la carte 
def film() :
    nom = bottle.request.forms.get('film')
    cor=(dico.get(nom))[0]
    adr=(dico.get(nom))[1]
    map = folium.Map(location=cor[0], tiles='OpenStreetMap', zoom_start=16)
    for j in range (len(cor)-1):
        folium.Marker(location=cor[j],popup=str(nom)+ ' //  adresse : '+str(adr[j])).add_to(map)
    map.save(outfile='map.html')
    file = open("map.html","r")
    Html  = file.read()
    return Html
bottle.run(bottle.app(), host='localhost', port=8080,debug=True, reloader=True)
    





