# Basic Flask REST API
My goal here was to create a really basic 
example for my students of a REST API built
using: Flask and SqlAlchemy.

## Getting Started
For this demo to work, you'll need access
to a database. I used MySQL with
an example database named bank. 
 
There aren't a lot of libraries that you'll
need to pip install for this example. I did
create a requirements.txt, so if you like, 
you could load an exact replica env using:

```
pip install -r requirements.txt
```

Really, the only libraries you should need are:

- sqlalchemy
- flask_sqlalchemy
- flask
- PyMySQL (though you could load the standard driver)
- cryptography (because PyMySQL needs it)

## Database setup
I used a locally installed MySQL DB server, with
a database named bank, with a single
table named customers. To access, I created a 
student user, with student as the password.
All of this is configurable of course.

**customers** table SQL script:

```
CREATE TABLE `customers` (
  `cust_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `email` varchar(120) NOT NULL,
  PRIMARY KEY (`cust_id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

If you check the config.py file, you'll find
and can configure the database connection URI, 
which includes (bad Patrick) the user and pass.

##Usage
This is a standard flask app. If you run it, the 
flask server should start, and print out which
port it's running on (5000 on my machine). 

Valid URL's, and input/response:

URL | Verb | Input JSON (if any) | Response
--- | --- | --- | ---
/ | GET | N/A | Returns a simple "Hello World!" message as a server test
/books | GET | N/A | JSON list of books (hard coded)
/book | POST | A JSON book object (use same format as one of the books returned by /books) | Success or error message and HTTP status
/customers | GET | N/A | JSON list of customers (don't forget to add some examples to your database!)
/customer/<cust_id> | GET | N/A | A single customer as JSON
/customer | POST | A JSON customer object (use same format as a customer from the customer list. The cust_id will be ignored if provided | Success or failure message

##Key components:
### config.py
Here's where you'll find the database URI. I'm going really basic
and have the username and password right in the config file. Fine 
for testing but please don't take it to production. You can update
the URI to suite your needs. 

###app.py
This is the main Flask based application driver. You can run it to start
the flask web server. Here's where you'll find all the route and verb
mappings.

### data_access.BookDAO
Class contains a couple of methods to get a list of books and add a new book. 
The book list is hard coded in the class file.

### data_access.models
Contains the Customer class, which is designed to work with
SqlAlchemy. Besides the standard Column setup, data attributes,
and constructor, you'll also find a couple of helper serialize/deserialize static methods. 

### data_access.CustomerDAO
Here you'll find the data access object that drives the 
customer related functionality. Besides methods to get a list of books, get a book,
and to add a book, you'll find some variations
 designed to work better with JSON.
