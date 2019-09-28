from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy

from config import Config
from data_access.BookDAO import BookDAO
from data_access.CustomerDAO import CustomerDAO

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

book_dao = BookDAO()
customer_dao = CustomerDAO(db)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/customers")
def get_customers():
    custs = customer_dao.get_customers_jsonable()
    return make_response(jsonify(custs))

@app.route("/customer/<cust_id>")
def get_customer(cust_id):
    cust = customer_dao.get_a_customer_jsonable(cust_id)
    return make_response(jsonify(cust))


@app.route("/customer", methods=["POST"])
def new_customer():
    if request.is_json:
        cust_dict = request.get_json()
        customer_dao.add_customer_from_dict(cust_dict)
        return "Customer added", 200

    else:
        return "Request was not JSON", 400


@app.route('/books')
def return_books():
    res = make_response(jsonify(book_dao.get_books()))
    return res


@app.route("/book", methods=["POST"])
def new_book():
    if request.is_json:
        book = request.get_json()
        # print(book)
        book_dao.add_book(book)

        return "Book loaded", 200

    else:
        return "Request was not JSON", 400


if __name__ == '__main__':
    app.run()
