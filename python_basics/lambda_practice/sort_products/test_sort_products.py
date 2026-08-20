import unittest

from sort_products import (
    get_product_names,
    sort_products_by_name,
    sort_products_by_price,
)


class SortProductsTests(unittest.TestCase):
    def test_sort_products_by_price(self):
        products = [
            {"name": "Book", "price": 20},
            {"name": "Pen", "price": 5},
            {"name": "Laptop", "price": 1000},
        ]

        result = sort_products_by_price(products)

        self.assertEqual(
            result,
            [
                {"name": "Pen", "price": 5},
                {"name": "Book", "price": 20},
                {"name": "Laptop", "price": 1000},
            ],
        )

    def test_sort_products_by_name(self):
        products = [
            {"name": "laptop", "price": 1000},
            {"name": "Book", "price": 20},
            {"name": "pen", "price": 5},
        ]

        result = sort_products_by_name(products)

        self.assertEqual(
            result,
            [
                {"name": "Book", "price": 20},
                {"name": "laptop", "price": 1000},
                {"name": "pen", "price": 5},
            ],
        )

    def test_get_product_names(self):
        products = [
            {"name": "Book", "price": 20},
            {"name": "Pen", "price": 5},
        ]

        result = get_product_names(products)

        self.assertEqual(result, ["Book", "Pen"])

    def test_empty_list_returns_empty_list(self):
        self.assertEqual(sort_products_by_price([]), [])
        self.assertEqual(sort_products_by_name([]), [])
        self.assertEqual(get_product_names([]), [])


if __name__ == "__main__":
    unittest.main()
