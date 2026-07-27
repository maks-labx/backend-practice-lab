class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        self._validate_positive_number(price, "Price")
        self._validate_positive_number(quantity, "Quantity")

        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {
                "price": price,
                "quantity": quantity,
            }

    def remove_item(self, name, quantity=1):
        self._validate_positive_number(quantity, "Quantity")

        if name not in self.items:
            raise ValueError("Item not found")

        if quantity > self.items[name]["quantity"]:
            raise ValueError("Not enough items in cart")

        self.items[name]["quantity"] -= quantity

        if self.items[name]["quantity"] == 0:
            del self.items[name]

    def get_total(self):
        total = 0

        for item in self.items.values():
            total += item["price"] * item["quantity"]

        return total

    def get_item_count(self):
        total_quantity = 0

        for item in self.items.values():
            total_quantity += item["quantity"]

        return total_quantity

    def _validate_positive_number(self, value, field_name):
        if value <= 0:
            raise ValueError(f"{field_name} must be greater than 0")
