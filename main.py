from customer import Customer
from admin import Admin
from restaurant import Restaurant
if __name__ == "__main__":
    
    restaurant = Restaurant("Tasty Delights")

    admin = Admin(restaurant)

    admin.create_menu_item("Pizza", 250)
    admin.create_menu_item("Burger", 150)
    
    admin.add_customer_account("Alice", "alice@example.com", "123 Street")
    
    customer = restaurant.customers["alice@example.com"]
    customer.view_menu(restaurant)
    
    customer.add_funds(500)
    
    customer.place_order(restaurant, "Pizza")
    
    customer.view_past_orders()
    
    admin.remove_customer_account("alice@example.com")
    
    
    admin.update_menu_item("Pizza", 300)
    
    admin.view_all_customers()
