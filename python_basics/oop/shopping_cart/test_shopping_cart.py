import unittest

from shopping_cart import ShoppingCart


class ShoppingCartTests(unittest.TestCase):
    def test_add_item_adds_item_to_cart(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20)

        self.assertEqual(
            cart.items,
            {
                "Book": {
                    "price": 20,
                    "quantity": 1,
                }
            },
        )

    def test_add_item_with_quantity(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20, quantity=3)

        self.assertEqual(cart.items["Book"]["quantity"], 3)

    def test_adding_existing_item_increases_quantity(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20, quantity=2)
        cart.add_item("Book", 20, quantity=1)

        self.assertEqual(cart.items["Book"]["quantity"], 3)

    def test_get_total_returns_sum_with_quantities(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20, quantity=2)
        cart.add_item("Pen", 5, quantity=3)

        self.assertEqual(cart.get_total(), 55)

    def test_remove_item_decreases_quantity(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20, quantity=3)
        cart.remove_item("Book", quantity=1)

        self.assertEqual(cart.items["Book"]["quantity"], 2)

    def test_remove_item_deletes_item_when_quantity_becomes_zero(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20, quantity=2)
        cart.remove_item("Book", quantity=2)

        self.assertEqual(cart.items, {})

    def test_get_item_count_returns_total_quantity(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20, quantity=2)
        cart.add_item("Pen", 5, quantity=3)

        self.assertEqual(cart.get_item_count(), 5)

    def test_cannot_add_item_with_invalid_price_or_quantity(self):
        cart = ShoppingCart()

        with self.assertRaises(ValueError):
            cart.add_item("Book", 0)

        with self.assertRaises(ValueError):
            cart.add_item("Book", 20, quantity=0)

    def test_remove_unknown_item_raises_error(self):
        cart = ShoppingCart()

        with self.assertRaises(ValueError):
            cart.remove_item("Book")

    def test_cannot_remove_more_than_available_quantity(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20, quantity=1)

        with self.assertRaises(ValueError):
            cart.remove_item("Book", quantity=2)


if __name__ == "__main__":
    unittest.main()
