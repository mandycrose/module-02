# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:43:21 2019

@author: mindy
"""

from flask import Flask,render_template,request
app = Flask("MyApp")

@app.route("/")
def hello():
    return "<h1>Hello London</h1>"

#@app.route("/bio")
#def  bio():
#    return "<h1>this is the bio page</h1>"

@app.route("/contact")
def contact():
    return "<h1>this is contact page</h1>"

@app.route("/bio")
def katherine():
    return render_template("katherine.html")

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name = name.title())

app.run(debug = True) 

