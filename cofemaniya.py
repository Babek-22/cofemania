class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CoffeeOrder:
    def __init__(self):
        self.menu = [
            Coffee("Espresso", 2.5),
            Coffee("Cappuccino", 3.0),
            Coffee("Latte", 3.5),
            Coffee("Mocha", 4.0),
        ]
        self.orders = []

    def display_menu(self):
        print("Menu:")
        for i, coffee in enumerate(self.menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price:.2f}")

    def take_order(self):
        self.display_menu()
        while True:
            try:
                choice = int(input("Enter the number of your choice (0 to finish): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(self.menu):
                    coffee = self.menu[choice - 1]
                    quantity = int(input(f"How many {coffee.name} would you like to order? "))
                    if quantity > 0:
                        self.orders.append((coffee, quantity))
                    else:
                        print("Quantity should be greater than 0.")
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def calculate_total(self):
        total = sum(coffee.price * quantity for coffee, quantity in self.orders)
        return total

    def print_receipt(self):
        print("\nReceipt:")
        for coffee, quantity in self.orders:
            print(f"{coffee.name} x{quantity}: ${coffee.price * quantity:.2f}")
        total = self.calculate_total()
        print(f"Total: ${total:.2f}")

    def run(self):
        print("Welcome to the Coffee Order App!")
        self.take_order()
        self.print_receipt()
        print("Thank you for ordering with us!")


if __name__ == "__main__":
    coffee_order_app = CoffeeOrder()
    coffee_order_app.run()
