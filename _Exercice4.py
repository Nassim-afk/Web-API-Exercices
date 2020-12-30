#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:29:40 2019

@author: nassim
"""


import xml.etree.ElementTree as ET 
from lxml import etree
tree=ET.parse('cd_catalog.xml')

root=tree.getroot()
print(root.tag) #tag de la racine 
print(root.attrib) #attribue de la racine 
#print(root[1][1].text) #CD=i ,attrib=j

#1**************************************Affichage COmplet
print('******************************ici*******************************')

print('-----------------TITLE')
for child in root :
    for title in child.iter('TITLE'):
        print(title.text)

print('-----------------ARTIST')        
for child in root :
    for artist in child.iter('ARTIST'):
        print(artist.text)

print('-----------------COUNTRY')
for child in root :
    for country in child.iter('COUNTRY'):
        print(country.text)

print('-----------------COMPANY')
for child in root :
    for company in child.iter('COMPANY'):
        print(company.text)
print('-----------------PRICE')
for child in root :
    for price in child.iter('PRICE'):
        print(price.text)
print('-----------------YEAR')
for child in root :
    for year in child.iter('YEAR'):
        print(year.text)
        
print('*********************************ici****************************')
#2.***************Affichage des CDs des années 80 

for child in root:
    for year in child.iter('YEAR'):
        if 1979<int(year.text)<1990 :
            for title in child.iter('TITLE'):
                print('lalbum',title.text,'est sorti en :',year.text)
                
print('*********************************ici****************************')             
                
#3.*************************les CDs anglais 
                
for child in root: #entre en <CD>
    for country in child.iter('COUNTRY'): #entre en <COUNTRY>
        if country.text=='UK':
            for title in child.iter('TITLE'):
                print('lalbum',title.text,'est dorigine :',country.text,'\n')
        


#1**************************************Affichage COmplet 2Éme méthode

"""  
print('*************************************************************')
print('---------sous la racine ')
#for child in root :
#   print(child.tag, child.attrib)
print('-----------------TITLE')
for title in root.iter('TITLE') :
    #print(title.tag,title.attrib,title.text) #TAG==> <catégorie> ,attrib==> {}
    print(title.text)
    
print('--------------------ARTIST')
for ARTIST in root.iter('ARTIST') :
    print(ARTIST.text)
    
print('--------------------COUNTRY')
for COUNTRY in root.iter('COUNTRY') :
    print(COUNTRY.text)

print('--------------------COMPANY')
for COMPANY in root.iter('COMPANY') :
    print(COMPANY.text)
print('--------------------price')
for PRICE in root.iter('PRICE') :
    print(PRICE.text)
print('--------------------YEAR')
for YEAR in root.iter('YEAR') :
    print(YEAR.text)
    
print('*************************************************************')
"""
#2.***************Affichage des CDs des années 80 
"""
   print(YEAR.text)
    if 1979<int(i[5].text)<1990 :
        print("le titre du cd est : \n",i[0].text)
   

for i in tree.xpath("/CATALOG/CD"):

    #print(type(YEAR.text))
    
    if 1979<int(i[5].text)<1990 :
        
        print("le titre du cd est : \n",i[0].text)
        print("****")
        
"""     