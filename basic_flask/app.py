from flask import Flask, jsonify, Response
from flask import request
import json



app = Flask(__name__)

books = [
    {'name': 'book1',
     'price': '12.99',
     'isbn': '1235532',
     },
    {'name': 'book2',
     'price': '13.99',
     'isbn': '442',
     }
]

def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

@app.route('/')
def hello_world():
    return ('Hello flask')

@app.route('/books')
def get_books():
    return (jsonify({'books':books}))

@app.route('/books/<isbn>')
def get_by_isbn(isbn):
    print(isbn)
    return_value ={}
    for book in books:
        if book["isbn"] == isbn:
            print(">>>>>>>>correct")
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
        else:
            print("false")
    return jsonify(return_value)

@app.route('/books',methods = ['POST'])
def add_new_book():
    requests_data = request.get_json()
    if(validBookObject(requests_data)):
        new_book = {
            "name":requests_data["name"],
            "price":requests_data["price"],
            "isbn":requests_data["isbn"]
        }
        books.insert(0,requests_data)
        response = Response("",201,mimetype='application/json')

        validBookObjectmsg = ({
            "Gotit": "Your book is created"
        })
        response = Response(json.dumps(validBookObjectmsg), status=201, mimetype='application/json')
        response.headers['Location'] = "/books/" + str(new_book['isbn'])
        return response
    else:
        invalidBookObjectErrorMsg = {
            "error" : "Invalid book object"
        }
        response = Response(json.dumps(invalidBookObjectErrorMsg),status = 400,mimetype='application/json')
        return response

@app.route('/books/<isbn>',methods = ['PUT'])
def update_book(isbn):
     request_data = request.get_json()
     new_book = {
         'name': request_data['name'],
         'price': request_data['price'],
         'isbn': isbn
     }
     i = 0
     for book in books:
         currentIsbn = book["isbn"]
         if currentIsbn == isbn:
             books[i] = new_book
         i += 1
     response = Response("",status = 204)
     return response


@app.route('/books/<isbn>',methods = ['PATCH'])
def update_book2(isbn):
    request_data = request.get_json()
    update_book = {}
    if ('name' in request_data):
        update_book["name"] = request_data['name']
    if ('price' in request_data):
        update_book["price"] = request_data['price']
    for book in books:
        if book["isbn"] == isbn:
            book.update(update_book)
    response = Response("",status="204")
    response.headers['location'] = "/books/" + str(isbn)
    return response

@app.route('/books/<isbn>',methods = ['DELETE'])
def delete_book(isbn):
    i = 0
    for book in books:
        if book["isbn"] == isbn:
            books.pop(i)
            response = Response("",status = 204)
            i+=1
        else:
            invalidBookObjecterrorMsg = {
                'error': "Book with ISBN number that provided was not found"
            }
            response = Response(json.dumps(invalidBookObjecterrorMsg),status = 404,mimetype = 'aplication/json')
    return response







app.run(port=5000)
