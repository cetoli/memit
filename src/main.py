#! /usr/bin/env python
# -*- coding: UTF8 -*-
"""
############################################################
Memit - Main
############################################################

:Author: *Carlo E. T. Oliveira*
:Contact: carlo@nce.ufrj.br
:Date: 2013/05/24
:Status: This is a "work in progress"
:Revision: 0.1.0
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
from datetime import datetime
from bottle import route, view, run, get, post, static_file, template, request
import bottle
import os
from couchdb import Server
import database
import json
DIR = os.path.dirname(__file__)+'/'
ADM, HEA, PEC, PHA, END = 'adm1n head peca fase fim'.split()

LIBS = DIR + '../libs/lib'
IMGS = DIR + 'studio/memit'

@route('/')
@view(DIR+'meme')
def main():
    try:
        doc_id, doc_rev = database.DRECORD.save({'type': 'Memit', 'date': str(datetime.now())})

        return dict(doc_id = doc_id)
    except Exception:
        return "Error in Database %s"%str([r for r in database.DRECORD])
        pass

@get('/<filename:re:.*\.html>')
def html(filename):
    return static_file(filename, root = DIR)

@get('/<filename:re:.*\.js>')
def javascript(filename):
    print(filename, '../libs/lib')
    return static_file(filename, root = LIBS)

@get('/<filename:re:.*\.py>')
def python(filename):
    return static_file(filename, root = DIR)

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def imagepng(filename):
    return static_file(filename, root = DIR)

def retrieve_data(req):
    jdata = req['data']
    print (jdata)
    return json.loads(jdata)


@post('/record/head')
def record_head():
    json = retrieve_data(request.params)
    try:
        record_id = json.keys()[0]
        print(json[record_id],record_id)
        record = database.DRECORD[record_id]
        print('record:',record)
        record[HEA]=json[record_id]
        record[PEC]=[]
        record[PHA]=[]
        database.DRECORD[record_id] = record
        return record
    except Exception:
        return "Cabeçalho não foi gravado %s"%str(request.params.values())#str([p for p in request.params])

@post('/record/piece')
def record_piece():
    try:
        json = retrieve_data(request.params)
        record_id = json.keys()[0]
        record = database.DRECORD[record_id]
        record[PEC] +=[json[record_id]]
        database.DRECORD[record_id] = record
        return record
    except Exception:
        return "Movimento de peça não foi gravado %s"%str(request.params.values())


@post('/record/phase')
def record_phase():
    try:
        json = retrieve_data(request.params)
        record_id = json.keys()[0]
        record = database.DRECORD[record_id]
        record[PHA] +=[json[record_id]]
        database.DRECORD[record_id] = record
        return record
    except Exception:
        return "Fase dd jogo não foi gravado %s"%str(request.params.values())

@post('/record/end')
def record_end():
    try:
        json = retrieve_data(request.params)
        record_id = json.keys()[0]
        record = database.DRECORD[record_id]
        record[END] =json[record_id]
        database.DRECORD[record_id] = record
        return record
    except Exception:
        return "Fim de jogo não foi gravado %s"%str(request.params.values())


if __name__ == "__main__":
    run(server='gunicorn', host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True, workers=1)

app = bottle.default_app()
