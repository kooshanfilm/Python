from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name=""):
    #name = request.args.get('name',name)
    return render_template("index.html",name= name)

# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1,num2):
#     return '{} + {} = {}'.format(num1,num2,num1+num2)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
     # return """
     # <!doctype html>
     # <html>
     # <head><title> Addidng </title></head>
     # <body>
     # <h1> {} + {} = {}</h1>
     # </body>
     # </html>
     # """.format(num1,num2,num1+num2)
     #
    context = {'num1':num1 ,'num2':num2}
    return render_template("add.html",**context)

#you can reload the page
app.run(debug = True)

