#!/usr/bin/python

from flask import Flask
app = Flask(__name__)

@app.route('/')

def general (f):
    f = raw_input('introduzca su frase: ')
    cortar = f.split(" ")

    cortar.reverse()

    str(cortar)

    final = ' '.join(cortar)

    print (final)
