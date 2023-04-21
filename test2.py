import unittest

from Shoppingcart import Cart

class TestCart(unittest.TestCase):

    def test_add(self):
        cart = Cart()
        cart.add()
        self.assertEqual(cart.grocery_dict, {"pineapple": {"price": 4.99, "quantity": 1}})

    def test_remove_it_if_not_in_the_cart_yet(self): #remove an item that isn't in the cart
        cart = Cart()
        cart.grocery_dict = {"kiwi": {"price": 2.99, "quantity": 3}}
        cart.remove()
        self.assertEqual(cart.testvariable2, "Item not in list")

    def test_remove(self): #remove an item in my cart
        cart = Cart()
        cart.grocery_dict = {"oranges": {"price": 2.99, "quantity": 8}}
        cart.remove()
        self.assertEqual(cart.grocery_dict, {"oranges": {"price": 2.99, "quantity": 5}})

if __name__ == '__main__':
    unittest.main()        