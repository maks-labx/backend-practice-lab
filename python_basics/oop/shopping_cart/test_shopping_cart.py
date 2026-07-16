import unittest

from shopping_cart import ShoppingCart


class ShoppingCartTests(unittest.TestCase):
    def test_add_item_adds_item_to_cart(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20)

        self.assertEqual(cart.items, [{"name": "Book", "price": 20}])

    def test_get_total_returns_sum_of_item_prices(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20)
        cart.add_item("Pen", 5)

        self.assertEqual(cart.get_total(), 25)

    def test_remove_item_removes_item_by_name(self):
        cart = ShoppingCart()

        cart.add_item("Book", 20)
        cart.add_item("Pen", 5)
        cart.remove_item("Book")

        self.assertEqual(cart.items, [{"name": "Pen", "price": 5}])

    def test_cannot_add_item_with_zero_or_negative_price(self):
        cart = ShoppingCart()

        with self.assertRaises(ValueError):
            cart.add_item("Book", 0)

        with self.assertRaises(ValueError):
            cart.add_item("Pen", -5)

    def test_remove_unknown_item_raises_error(self):
        cart = ShoppingCart()

        with self.assertRaises(ValueError):
            cart.remove_item("Book")


if __name__ == "__main__":
    unittest.main()