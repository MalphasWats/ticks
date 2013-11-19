# Web App
# Web App
from flask import render_template

from ticks import app

@app.route('/')
def webapp():
    return render_template('layout.html')