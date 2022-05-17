from flask import Flask

app = Flask(__name__)

#Members API Route

@app.route("/books")
def books():
    # return {"books": [{"name":"Deepak"}, {"name":"Deepak"}]}

    return {"books" : [{"id": 1 ,"name": "Book1", "author":"Author1", "releasedate":"10-05-2022", "isbn": 234544287, "img":"https://images-na.ssl-images-amazon.com/images/I/81Lb75rUhLL.jpg"},
     {"id": 2,"name": "Book1", "author":"Author1", "releasedate":"10-05-2022", "isbn": 234544287, "img":"https://images-na.ssl-images-amazon.com/images/I/81Lb75rUhLL.jpg"},
     {"id": 3,"name": "Book1", "author":"Author1", "releasedate":"10-05-2022", "isbn": 234544287, "img":"https://images-na.ssl-images-amazon.com/images/I/81Lb75rUhLL.jpg"},{"id": 4,"name": "Book1", "author":"Author1", "releasedate":"10-05-2022", "isbn": 234544287, "img":"https://images-na.ssl-images-amazon.com/images/I/81Lb75rUhLL.jpg"},{"id": 5,"name": "Book1", "author":"Author1", "releasedate":"10-05-2022", "isbn": 234544287, "img":"https://images-na.ssl-images-amazon.com/images/I/81Lb75rUhLL.jpg"},{"id": 6,"name": "Book1", "author":"Author1", "releasedate":"10-05-2022", "isbn": 234544287, "img":"https://images-na.ssl-images-amazon.com/images/I/81Lb75rUhLL.jpg"}, ]}

if __name__ == "__main__":
    app.run(debug=True)