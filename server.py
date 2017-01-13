from flask import Flask
from flask import render_template

app = Flask(__name__)

import os

files_path = './uploads/'

@app.route('/')
def index():

    files = os.listdir( files_path )
    files = filter( lambda x: x.endswith('.py'), files )
    files = map( lambda x: x.replace('.py', ''), files )

    return render_template('index.html', files = files)

if __name__ == "__main__":
    app.run()
