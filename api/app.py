from flask import Flask
from mongoengine import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World, I am here'
