# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
def index():
    message = "Let's Beat the Bookies Together"
    return render_template('index.html', message=message)