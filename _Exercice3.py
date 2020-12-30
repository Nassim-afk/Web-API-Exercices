#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 18:35:32 2019

@author: nassim
"""
import json


#with open('tournagesdefilmsparis2011.json') as file :
decoded=json.load(open('tournagesdefilmsparis2011.json'))
    
#Afficher les entrées demandés *********************************

a,b,c,d,e,=[],[],[],[],[]
dico={}



for i in decoded:   #entrer dans ce que je décode
    info=i['fields']   # m'interesse qu'à la section fields
    #print(i['realisateur'])
    print('le realisateur est :\n',info.get('realisateur'))
    print('le titre est :\n',info.get('titre'))
    print('adresse :\n',info.get('adresse'),info.get('ardt'))
    print('la date de début est:\n',info.get('date_debut'))
    print('la date de fin  est :\n',info.get('date_fin'))
    print('les coordonnées sont :\n',info.get('xy'))
    print('*****************************************')
    
    #j'ajoute pour plus tard les entrés dans des listes initialement vide
    
    a.append(info.get('realisateur')) 
    b.append(info.get('titre'))
    c.append(info.get('ardt'))
    d.append(info.get('date_debut'))
    e.append(info.get('adresse'))
    
    
#2-Affichage******************************************
#Enlever les entrés multiples des réalisateurs

rea=list(a)

rea_list=[]
for i in rea:
    rea_list.append(i)
    r=rea.count(i) #avoir le nbr de fois qu'un nom se répéte 

    for j in range(r-1):
        rea.remove(i) #j'enléve ce réalisateur de la liste mére r-1 fois
                        #si le nom se répéte 14 fois je l'enléve 13 fois
                        
#Enlever les entrés multiples des titres de films*************
                        
title=list(b) 
title_list=[]
for i in title:
    title_list.append(i)
    t=title.count(i)
    
    for j in range(t-1):
        title.remove(i)

#Création du dictionnaire
date=[]
adresse=[] #initialisation vide
arondi=[]

for i in title_list :
    f=[]
    g=[]
    h=[]
    for j in range (len(b)):
        if i == b[j]: #si le titre coincide avec son realisateur
            f.append(d[j]) #date
            g.append(e[j]) #adresse
            h.append(c[j]) #arrondissement 
    date.append(tuple(f))
    adresse.append(tuple(g))
    arondi.append(tuple(h))
    

dico['titre']=title_list
dico['realisateur']=rea_list
dico['date']=date
dico['adresse']=adresse
dico['arrondissement']=arondi

def Affichage (film):
    i=title_list.index(film)
    print(" \nla date de tournage du film ",film,"sont :",dico['date'][i])
    print("le réalisateur de ce film est \n :",dico['realisateur'][i])
    print("les lieux de tournage sont \n :",dico['adresse'][i])

film=input('quel film cherchez-vous ? ( tapez en majiscule) ')
film=str(film)
Affichage(film)
print("******************************************")

def Localisation_tournage (film) :
    i=title_list.index(film)
    count=b.count(film)
    print("le nombre de tournages \n :",count)
    print("les arrondissements \n: ",dico['arrondissement'][i])
    
Localisation_tournage(film)


        
        