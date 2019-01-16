# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:12:03 2019

@author: mindy
"""
from flask import Flask, render_template,request
app = Flask("MyApp")
@app.route("/katherine")
def katherine_homepage():
    return "hello"
app.run(debug = True) 

#render_template("index.html", name = name.title())