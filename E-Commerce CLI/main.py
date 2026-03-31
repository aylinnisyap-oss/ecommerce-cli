import json

def load_products():
    with open("products.json", "r") as f:
        return json.load(f)

def load_cart():
    with open("cart.json", "r") as f:
        return json.load(f)

def save_cart(cart):
    with open("cart.json", "w") as f:
        json.dump(cart, f, indent=4)


def view_products(products):
    print("\nAvailable Products:")
    for p in products:
        print(f"{p['id']}. {p['name']} - ₹{p['price']}")

def search_product(products):
    keyword = input("Enter product name: ").lower()
    found = False

    for p in products:
        if keyword in p['name'].lower():
            print(f"{p['id']}. {p['name']} - ₹{p['price']}")
            found = True

    if not found:
        print("No product found")

def add_to_cart(products, cart):
    try:
        pid = int(input("Enter product ID: "))
        for p in products:
            if p['id'] == pid:
                cart.append(p)
                save_cart(cart)
                print("Added to cart!")
                return
        print("Invalid product ID")
    except:
        print("Enter a valid number")

def view_cart(cart):
    print("\nYour Cart:")
    if not cart:
        print("Cart is empty")
        return

    total = 0
    for item in cart:
        print(f"{item['name']} - ₹{item['price']}")
        total += item['price']

    print(f"Total: ₹{total}")

def remove_from_cart(cart):
    try:
        pid = int(input("Enter product ID to remove: "))
        for item in cart:
            if item['id'] == pid:
                cart.remove(item)
                save_cart(cart)
                print("Removed from cart")
                return
        print("Item not in cart")
    except:
        print("Invalid input")

def checkout(cart):
    if not cart:
        print("Cart is empty")
        return

    total = sum(item['price'] for item in cart)
    print(f"Total amount: ₹{total}")
    confirm = input("Confirm order? (yes/no): ")

    if confirm.lower() == "yes":
        cart.clear()
        save_cart(cart)
        print("Order placed successfully!")
    else:
        print("Order cancelled")


def main():
    products = load_products()
    cart = load_cart()

    while True:
        print("\n===== E-Commerce CLI =====")
        print("1. View Products")
        print("2. Search Product")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            view_products(products)

        elif choice == "2":
            search_product(products)

        elif choice == "3":
            add_to_cart(products, cart)

        elif choice == "4":
            view_cart(cart)

        elif choice == "5":
            remove_from_cart(cart)

        elif choice == "6":
            checkout(cart)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

main()