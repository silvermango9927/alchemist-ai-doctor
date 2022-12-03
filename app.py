from flask import Flask, redirect, render_template, url_for
from row_matching import *

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'