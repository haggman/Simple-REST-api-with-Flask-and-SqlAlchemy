from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
'''
To use this class, you will need to manually create the DB in MySQL
such that it has a customers table which matches the below form. 
The create SQL script would be something like:
CREATE TABLE `customers` (
  `cust_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `email` varchar(120) NOT NULL,
  PRIMARY KEY (`cust_id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
'''


class Customer(Base):
    __tablename__ = 'customers'
    cust_id = Column(Integer, primary_key=True)
    first_name = Column(String(15))
    last_name = Column(String(15))
    email = Column(String(120))

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @staticmethod
    def as_dictionary(a_customer):
        return {
            'cust_id': a_customer.cust_id,
            'first_name': a_customer.first_name,
            'last_name': a_customer.last_name,
            'email': a_customer.email
        }

    @staticmethod
    def new_from_dictionary(cust_as_dict):
        return Customer(cust_as_dict["first_name"],
                        cust_as_dict["last_name"],
                        cust_as_dict["email"]
                        )

    def __repr__(self):
        return f'Customer<{self.first_name}, {self.last_name}>'
