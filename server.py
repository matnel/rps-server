from flask import *

app = Flask(__name__)

import os
import collections

files_path = './uploads/'

@app.route('/')
def index():

    files = os.listdir( files_path )
    files = filter( lambda x: x.endswith('.py'), files )
    files = map( lambda x: x.replace('.py', ''), files )

    return render_template('index.html', files = files)

@app.route('/execute', methods=['POST', 'GET'] )
def execute():

    first=request.form['first']
    second=request.form['second']

    results = [ first, second ]
    results = collections.Counter( results )

    return render_template('results.html', results = results )

@app.route('/save', methods=['POST', 'GET'] )
def save():

    name=request.form['filename'].strip()
    code=request.form['code'].strip()

    if not name.endswith( '.py' ):
        name += '.py'

    name = files_path + name

    open( name, 'w').write( code )

    return "Saved!"

if __name__ == "__main__":
    app.run()
