from customer import Customer

class Admin:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def create_menu_item(self, name, price):
 
        self.restaurant.add_menu_item(name, price)

    def remove_menu_item(self, name):
        
        self.restaurant.remove_menu_item(name)

    def add_customer_account(self, name, email, address):
    
        customer = Customer(name, email, address)
        self.restaurant.add_customer(customer)

    def view_all_customers(self):
   
        self.restaurant.view_all_customers()

    def remove_customer_account(self, email):
       
        self.restaurant.remove_customer_account(email)

    def update_menu_item(self, name, new_price):
        
        self.restaurant.update_menu_item(name, new_price)
