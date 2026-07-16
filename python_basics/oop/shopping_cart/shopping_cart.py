class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        if price <= 0:
            raise ValueError("Price must be greater than 0")

        item = {
            "name": name,
            "price": price,
        }

        self.items.append(item)

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return

        raise ValueError("Item not found")

    def get_total(self):
        total = 0

        for item in self.items:
            total += item["price"]

        return total