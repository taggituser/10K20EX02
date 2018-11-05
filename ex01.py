#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 13:59:38 2018

@author: taguser 
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Example page"

if __name__=='__main__':
    app.run(port=5000,debug=True)