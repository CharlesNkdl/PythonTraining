# Product Inventory Project - Create an application which manages an inventory of products.
# Create a product class which has a price, id, and quantity on hand.
# Then create an inventory class which keeps track of various products and can sum up the inventory value.

class Product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

    def __str__(self):
        return "Price: %s, ID: %s, Quantity: %s" % (self.price, self.id, self.quantity)


class Inventory:

    def __init__(self):
        self.inven = []

    def add_product(self, product):
        self.inven.append(product)

    def sum_inventory(self):
        summer = 0
        for prod in self.inven:
            summer += prod.price * prod.quantity
        return summer

    def print_inventory(self):
        for prod in self.inven:
            print(prod)


prod1 = Product(5, 1, 10)
prod2 = Product(10, 2, 5)
prod3 = Product(2, 3, 20)
inv1 = Inventory()
inv1.add_product(prod1)
inv1.add_product(prod2)
inv1.add_product(prod3)
inv1.print_inventory()
print("Total inventory value: %s" % inv1.sum_inventory())