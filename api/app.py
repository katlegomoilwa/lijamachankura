from flask import Flask
from mongoengine import connect

app = Flask(__name__)

connect(host='mongodb://localhost/lijamachankura')

@app.route('/')
def index():
    return 'Hello World, I am here'
