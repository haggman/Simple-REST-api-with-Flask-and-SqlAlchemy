from .models import Customer


class CustomerDAO:

    def __init__(self, db):
        self.db = db

    def add_customer(self, first_name, last_name, email):
        new_cust = Customer(first_name=first_name, last_name=last_name,
                            email=email)
        self.db.session.add(new_cust)
        self.db.session.commit()

    def add_customer_from_dict(self, new_customer_dict):
        new_cust = Customer.new_from_dictionary(new_customer_dict)
        self.db.session.add(new_cust)
        self.db.session.commit()

    def get_customers(self):
        return self.db.session.query(Customer).all()

    def get_customers_jsonable(self):
        return [Customer.as_dictionary(aCust) for aCust in self.get_customers()]


    def get_a_customer(self, cust_id):
        return self.db.session.query(Customer).get(cust_id)


    def get_a_customer_jsonable(self, cust_id):
        return Customer.as_dictionary(self.get_a_customer(cust_id))
