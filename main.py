# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:04:21 2017

@author: thomas
"""

from flask import Flask, render_template

#__name__ points to root path 
app = Flask(__name__)

@app.route('/')
def index():
   
     #here we would pass in a html template
     return render_template("test.html")


@app.route('/schlachtfeld')
def schlachtfeld():
     return render_template("wireframe.html")

#makes shure that we start the webserver when we run the file
if __name__ == "__main__":
     app.run()
   