#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:18:01 2019

@author: nassim
"""

import bottle
import requests
from html.entities import codepoint2name

def htmlCoding(stringToCode):
    return ''.join( '&%s;' % codepoint2name[ord(oneChar)]
                                            if ord(oneChar) in codepoint2name
                                            else oneChar for oneChar in stringToCode )
@bottle.route("/qui")

@bottle.view("page.tpl")

def qui():
    stri="""
    <form method='post' action='bonjour'>
    <input type='text'name='nom' placeholder='votre nom ?' />
    <input type='submit' value='Validez !'/>
    </form>
    """
    return {"title":"Présentez-vous", "body" : stri}

@bottle.route("/bonjour", method='POST')
@bottle.view("page.tpl")

def bonjour():
    nom=bottle.request.forms.nom
    stri = "Bonjour Madame/Monsieur "+htmlCoding(nom)
    return {"title":"Bonjour", "body" : stri}
    #return "Bonjour"+htmlcoding(nom)

bottle.run(bottle.app(),host='localhost',port=8080,debug=True, reloader=True)

