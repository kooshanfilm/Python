from flask import Flask
from flask import request
from flask import render_template
from flask import redirect, url_for,make_response
import pdb
import json

app = Flask(__name__)

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('my_saved'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html',saves = data)

@app.route('/save',methods = ['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('my_saved',json.dumps(data))
    return response

@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves = get_saved_data()
    )

#you can reload the page
app.run(debug = True)

