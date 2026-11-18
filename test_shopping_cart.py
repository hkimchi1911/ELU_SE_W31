
import unittest
from shopping_cart import calculate_total


class TestShoppingCart(unittest.TestCase):

    def test_calculate_total(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]

        self.assertAlmostEqual(calculate_total(cart), 25.47)

    def test_empty_cart(self):
        self.assertEqual(calculate_total([]), 0.0)


if __name__ == '__main__':
    unittest.main()
