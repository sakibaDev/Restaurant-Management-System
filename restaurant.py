class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}  # {item_name: price}
        self.customers = {}  # {email: Customer object}

    def add_menu_item(self, name, price):
        
        self.menu[name] = price
        print(f"{name} added to menu at {price} taka.")

    def remove_menu_item(self, name):
        
        if name in self.menu:
            del self.menu[name]
            print(f"{name} removed from menu.")
        else:
            print(f"{name} not found in the menu.")

    def show_menu(self):
        
        print(f"_____Menu of {self.name}_____")
        for name, price in self.menu.items():
            print(f"{name}: {price} taka")

    def add_customer(self, customer):
        
        self.customers[customer.email] = customer
        print(f"Customer {customer.name} added.")

    def remove_customer_account(self, email):
        
        if email in self.customers:
            del self.customers[email]
            print(f"Customer with email {email} removed.")
        else:
            print(f"Customer with email {email} not found.")

    def update_menu_item(self, name, new_price):
    
        if name in self.menu:
            self.menu[name] = new_price
            print(f"Price of {name} updated to {new_price}.")
        else:
            print(f"{name} not found in the menu.")

    def view_all_customers(self):
        
        if self.customers:
            print("List of customers:")
            for email, customer in self.customers.items():
                print(f"{customer.name} - {email}")
        else:
            print("No customers found.")
