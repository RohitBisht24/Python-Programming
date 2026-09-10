class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id


class Customer(User):
    def __init__(self, name, user_id):
        super().__init__(name, user_id)
        self.cart = []
        self.discount_percent = 0

    def add_product(self, product_name, price):
        self.cart.append({"name": product_name, "price": price})
        print(f"{product_name} cart me add ho gaya.")

    def remove_product(self, product_name):
        for product in self.cart:
            if product["name"].lower() == product_name.lower():
                self.cart.remove(product)
                print(f"{product_name} cart se remove ho gaya.")
                return

        print("Product cart me nahi mila.")

    def calculate_total(self):
        return sum(product["price"] for product in self.cart)

    def apply_coupon(self, discount_percent):
        if 0 <= discount_percent <= 100:
            self.discount_percent = discount_percent
            print(f"{discount_percent}% discount coupon apply ho gaya.")
        else:
            print("Invalid discount percentage.")

    def show_cart(self):
        if not self.cart:
            print("Cart empty hai.")
            return

        print("\n--- Your Cart ---")
        for product in self.cart:
            print(f"{product['name']} - Rs. {product['price']}")
        print("Total:", self.calculate_total())

    def place_order(self):
        if not self.cart:
            print("Cart empty hai. Order place nahi ho sakta.")
            return

        total = self.calculate_total()
        discount_amount = total * self.discount_percent / 100
        final_amount = total - discount_amount

        print("\n--- Order Placed Successfully ---")
        print("Customer Name:", self.name)
        print("User ID:", self.user_id)
        print("Total Amount: Rs.", total)
        print("Discount: Rs.", discount_amount)
        print("Final Amount: Rs.", final_amount)

        self.cart.clear()
        self.discount_percent = 0


# User-defined input
name = input("Enter your name: ")
user_id = input("Enter your user ID: ")

customer = Customer(name, user_id)

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Show Cart")
    print("4. Apply Coupon")
    print("5. Place Order")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product_name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        customer.add_product(product_name, price)

    elif choice == "2":
        product_name = input("Enter product name to remove: ")
        customer.remove_product(product_name)

    elif choice == "3":
        customer.show_cart()

    elif choice == "4":
        discount = float(input("Enter discount percentage: "))
        customer.apply_coupon(discount)

    elif choice == "5":
        customer.place_order()

    elif choice == "6":
        print("Thank you for shopping!")
        break1

    else:
        print("Invalid choice. Try again.")