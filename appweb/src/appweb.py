#!/usr/bin/python

import os,sys
import subprocess
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('Client request!')
    return 'Hello World'

def main():
    print('Server activated, port: 8080')
    serve(app, host="0.0.0.0", port=8080)
 
if __name__ == '__main__':
    main()
