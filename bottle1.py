#!/usr/bin/python
# -*- coding: utf-8 -*-
from bottle import route, run, get, post
import json
import requests

@route('/login')
def login():
    return ''' <form method="POST" action="/login">
                        <label>nombre de usuario</label><input name="name" type="text" />
                        <label>contraseña</label><input name="password" type="password" />
                   </form>'''

@post('/login', method='POST')
def enviar_form():
        name = request.forms.get('name')
        password = request.forms.get('password')
        if login(name, password):
                return "<p>login correcto</p>"
        else:
                return "<p>login incorrecto</p>"

@route('/getTidesInfo')
def getTidesInfo():
        API='tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'
        req = requests.get('http://servizos.meteogalicia.es/apiv2/getTidesInfo', params={'coord':'-8.637,43.45','API_KEY':API})
        response = json.loads(req.text)
        print response



@get('/findPlaces')
def findPlaces():
        API='tntmnZ85PrQ6AGw6ihuUGhqs894jl66UI8p4ph4rmbvcno3MIApKE0o2N1awzT2p'
        req = requests.get('http://servizos.meteogalicia.es/apiv2/findPlaces', params={'location':'%s','API_KEY':API})
        response = json.loads(req.text)
        print response['type']




















run(host='localhost', port=8080, debug=True)
