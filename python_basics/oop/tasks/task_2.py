class Product:
    def __init__(self, name, price):
        self.price = price
        self.name = name

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("The price must not be negative")
        else:
            self._price = value

product = Product("Laptop", 5000)

print(product.name)
print(product.price)

product.price = 4500
print(product.price)

product.price = -100