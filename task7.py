import random
from prettytable import PrettyTable

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self):
        self.products = self.read_products()
        
    def read_products(self):
        return [
            Product("Notebook", 50.0, 500),
            Product("Pen", 10.0, 1000),
            Product("Pencil", 5.0, 1500),
            Product("Eraser", 3.0, 800),
            Product("Ruler", 20.0, 300)
        ]

    def print_product_table(self):
        product_table = PrettyTable()
        product_table.field_names = ["Name", "Price", "Quantity"]
        for product in self.products:
            product_table.add_row([product.name, product.price, product.quantity])
        print("\nProducts Available:")
        print(product_table)

    def get_product_choice(self):
        total_discounted_price = 0
        while True:
            product_name = input("Enter Product Name: ").lower()
            product = next((p for p in self.products if p.name.lower() == product_name), None)

            if product is None:
                print("Product not found in the table. Please enter a valid product.")
                continue

            quantity_required = float(input("Enter Quantity Required: "))
            if quantity_required > product.quantity:
                print("Insufficient quantity. Please enter a new quantity.")
                continue

            discount_quantity = quantity_required // 250
            discount_percentage = min(5.0 * discount_quantity, 25.0)
            discounted_price = quantity_required * product.price * (1 - discount_percentage / 100)
            product.quantity -= quantity_required
            total_discounted_price += discounted_price

            print(f"Discounted Price: ${discounted_price:.2f}")
            another_item = input("Do you want to add another item? (yes/no): ")
            if another_item.lower() != 'yes':
                break

        return total_discounted_price

    def stationary_store(self):
        total_stationary_price = 0
        while True:
            stationary_name = input("Enter Stationary Product Name: ").lower()
            product = next((p for p in self.products if p.name.lower() == stationary_name), None)

            if product is None:
                print("Product not found in the stationary store. Please enter a valid product.")
                continue

            stationary_quantity_required = float(input("Enter Quantity Required: "))
            if stationary_quantity_required > product.quantity:
                print("Insufficient quantity. Please enter a new quantity.")
                continue

            loyalty_discount_quantity = stationary_quantity_required // 50
            stationary_discounted_price = stationary_quantity_required * product.price * (1 - 2.0 * loyalty_discount_quantity / 100)
            total_stationary_price += stationary_discounted_price
            product.quantity -= stationary_quantity_required

            print(f"Discounted Price: ${stationary_discounted_price:.2f}")
            another_stationary_item = input("Do you want to add another stationary item? (yes/no): ")
            if another_stationary_item.lower() != 'yes':
                break

        return total_stationary_price

    def process_payment(self, total_discounted_price):
        delivery_option = input("Do you want delivery or pick-up? (Enter 'delivery' or 'pick-up'): ").lower()
        delivery_charge = 200
        pickup_charge = 50

        if delivery_option == 'delivery':
            total_discounted_price += delivery_charge
        elif delivery_option == 'pick-up':
            total_discounted_price += pickup_charge

        payment_currency = input("Choose a payment currency (USD, EUR, EGP): ").upper()
        usd_to_eur_rate = 0.92
        usd_to_egp_rate = 30.90

        if payment_currency == "USD":
            total_price_in_chosen_currency = total_discounted_price
        elif payment_currency == "EUR":
            total_price_in_chosen_currency = total_discounted_price * usd_to_eur_rate
        elif payment_currency == "EGP":
            total_price_in_chosen_currency = total_discounted_price * usd_to_egp_rate
        else:
            print("Invalid currency choice. Defaulting to USD.")
            total_price_in_chosen_currency = total_discounted_price

        print(f"\nTotal Discounted Price in {payment_currency}: ${total_price_in_chosen_currency:.2f}")

    def main(self):
        self.print_product_table()
        total_discounted_price = self.get_product_choice()
        visit_stationary_store = input("Do you want to visit our new stationary store? (yes/no): ")
        if visit_stationary_store.lower() == 'yes':
            total_stationary_price = self.stationary_store()
            total_discounted_price += total_stationary_price

        print(f"\nTotal Discounted Price (including stationary store): ${total_discounted_price:.2f}")
        self.process_payment(total_discounted_price)
        print("Your order is on the way!")

if __name__ == "__main__":
    store = Store()
    store.main()
