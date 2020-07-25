class Product:
    # Constructor
    def __init__(self, name, price, qoh=0):
        # Object Attributes
        self.name = name
        self.price = price
        self.qoh = qoh

    # Methods
    def print_details(self):
        print('Name  : ', self.name)
        print('Price : ', self.price)
        print('Qoh   : ', self.qoh)

    def sell(self, qty):
        self.qoh -= qty

    def purchase(self, qty):
        self.qoh += qty


p = Product("iPhone 11", 100000, 20)  # Create an object
print(type(p))
p.sell(5)
# p.disrate = 20
print(p.__dict__)
p.print_details()
p2 = Product("Dell Laptop XYZ", 75000)
p2.print_details()
