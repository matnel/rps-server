from flask import *
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

import json

users = json.load( open('users.json') , strict=False )

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

import os
import collections
import engine

files_path = './uploads/'

@app.route('/')
@auth.login_required
def index():

    files = os.listdir( files_path )
    files = filter( lambda x: x.endswith('.py'), files )
    files = map( lambda x: x.replace('.py', ''), files )

    return render_template('index.html', files = files)

@app.route('/execute', methods=['POST', 'GET'] )
@auth.login_required
def execute():

    first=request.form['first']
    second=request.form['second']

    results = engine.compare( first, second, files_path )
    results = collections.Counter( results )

    return render_template('results.html', results = results )

@app.route('/save', methods=['POST'] )
@auth.login_required
def save():

    name=request.form['filename'].strip()
    code=request.form['code'].strip()

    if not name.endswith( '.py' ):
        name += '.py'

    name = files_path + name

    open( name, 'w').write( code )

    return "Saved!"

if __name__ == "__main__":
    port = int( os.environ.get('PORT', 5000) )
    app.run( host='0.0.0.0', port=port, debug=True )
