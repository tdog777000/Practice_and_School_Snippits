class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none", total=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        self.total = total

    def print_item_cost(self):
        self.total = self.item_quantity * self.item_price
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.total))

    def print_item_description(self, ItemToPurchase):
        print("{}: {}".format(ItemToPurchase.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        self.cart_total = 0

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        signal = 0
        for items in self.cart_items:
            if item_name == items.item_name:
                self.cart_items.remove(items)
                signal = 1
                break
        if signal < 1:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, ItemToPurchase):
        signal = 0
        new = int(input("Enter the new quantity:\n"))
        for items in self.cart_items:
            if ItemToPurchase.item_name == items.item_name:
                items.item_quantity = new
                signal = 1
                break
        if signal < 1:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for items in self.cart_items:
            num_items += items.item_quantity
        return num_items

    def get_cost_of_cart(self):
        self.cart_total = 0
        for items in self.cart_items:
            self.cart_total = self.cart_total + (items.item_price * items.item_quantity)
        return self.cart_total

    def print_total(self):
        print("{}'s Shopping Cart - {}\nNumber of Items: {}\n".format(self.customer_name, self.current_date,
                                                                      self.get_num_items_in_cart()))
        if self.get_num_items_in_cart() > 0:
            for items in self.cart_items:
                items.print_item_cost()
        else:
            print("SHOPPING CART IS EMPTY")
        print("\nTotal: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("""{}'s Shopping Cart - {}

Item Descriptions""".format(self.customer_name, self.current_date))
        for items in self.cart_items:
            items.print_item_description(items)


def print_menu():
    print("""MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit\n""")


def execute_menu(choice, cart):
    if choice == "a":
        print("ADD ITEM TO CART")
        cart_item = ItemToPurchase()
        cart_item.item_name = input("Enter the item name:\n")
        cart_item.item_description = input("Enter the item description:\n")
        cart_item.item_price = int(input("Enter the item price:\n"))
        cart_item.item_quantity = int(input("Enter the item quantity:\n"))
        cart.add_item(cart_item)
        print()
    elif choice == "r":
        print("REMOVE ITEM FROM CART")
        cart_item = input("Enter name of item to remove:\n")
        cart.remove_item(cart_item)
        print()
    elif choice == "c":
        print("CHANGE ITEM QUANTITY")
        cart_item = ItemToPurchase()
        cart_item.item_name = input("Enter the item name:\n")
        cart.modify_item(cart_item)
        print()
    elif choice == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        cart.print_descriptions()
        print()
    elif choice == "o":
        print("OUTPUT SHOPPING CART")
        cart.print_total()
        print()


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.customer_name = input("Enter customer's name:\n")
    cart.current_date = input("Enter today's date:\n")
    print("\nCustomer name: {}\nToday's date: {}\n".format(cart.customer_name, cart.current_date))
    user_input = ""
    while True:
        print_menu()
        options = ["a", "r", "c", "i", "o", "q"]
        while user_input not in options:
            user_input = input("Choose an option:\n")
        if user_input != "q":
            execute_menu(user_input, cart)
            user_input = ""
        else:
            break
