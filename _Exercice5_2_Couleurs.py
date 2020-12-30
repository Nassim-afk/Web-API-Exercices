#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:21:45 2019

@author: nassim
"""
import bottle
import requests



Colors=['jaune','rouge','vert','bleu',]

@bottle.route("/qui")
@bottle.view("page.tpl")

def qui() :
    stri = """
    <form method='post' action='couleur'>
    <SELECT name = couleur>
    """
    for i in range(len(Colors)) :
        stri  += "<option>" + Colors[i] + "</option>"
    
    stri += "</SELECT><hr/><input type='submit' value='confirmer'/></FORM>"""
    return {"title":"Quel est votre couleur préféré :", "body" : stri}

@bottle.route("/couleur", method='POST')
@bottle.view("page.tpl")

def couleur() :
    return "Votre couleur préferé est la couleur " + bottle.request.forms.get('couleur')

bottle.run(bottle.app(), host='localhost', port=8081,debug=True, reloader=True)

