#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:39:29 2019

@author: nassim
"""

import re 
import requests 

print('Premiére question \n:')
Liste=["Marie.Dupond@gmail.com",
       "Lucie.Durand@wanadoo.fr",
       "Sophie.Parmentier@@gmail.com",
       "Franck.Dupres.gmail.com",
       "Pierre.Martin@lip6.fr",
       "Eric.Deschamps@gmail.com","Eric.Deschamps@gmaileeee.com"]

for i in Liste:
    mails= re.match('([^@]+)@([^@]+)',i)
    
    """none type object has no attribute"""
    """gerer l'exception"""
    if mails != None:
        print(mails.group())
print("***********************************************")
        
print('deuxieme question \n:') 
for i in Liste:
   chiffre=re.findall("(.+[0-9])", i)
   if chiffre != []:
       print(chiffre)
print("***********************************************'")

print('troisiéme question \n:')    
ip="216.08.094.196"
ips=ip.replace('0','')
print(ips)

print("***********************************************")
print("Quatrieme question")
date="10-02-2018" #02-10-2018

print(date)
date2=date.split('-')
date3=date2[0]
date4=date2[1]
print(date4,date3,date2[2])
"""par=re.match('([0-9])',date)
print(par.group())
"""



        
