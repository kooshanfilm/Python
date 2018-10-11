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


def get_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            # print(">>>>>>>>correct")
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }

    return (return_value)


print(get_by_isbn("442"))
