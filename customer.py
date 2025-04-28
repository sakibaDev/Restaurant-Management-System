class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0.0
        self.orders = []

    def view_menu(self, restaurant):
        restaurant.show_menu()

    def place_order(self, restaurant, item_name):
        if item_name in restaurant.menu:
            price = restaurant.menu[item_name]
            if self.balance >= price:
                self.balance -= price
                self.orders.append(item_name)
                print(f"Order placed: {item_name} for {price} taka. Remaining balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print(f"{item_name} is not on the menu.")

    def check_balance(self):
        print(f"Your current balance is {self.balance} taka.")

    def view_past_orders(self):
        if self.orders:
            print("___Your Order History___")
            for order in self.orders:
                print(f"- {order}")
        else:
            print("You haven't placed any orders yet.")

    def add_funds(self, amount):
        self.balance += amount
        print(f"Funds added: {amount} taka. New balance: {self.balance}")
