#!/usr/local/env python3
#Created By: J.Medlock
#Created On: 2017.09.07


class ShoppingCart(object):
    items_in_cart = {}
    def __init__(self, name):
        self.name = name

    def add_item(self, item, price):
        if not item in self.items_in_cart:
            self.items_in_cart[item] = price
            print(item + " added!")
        else:
            print(item + " item is already in the cart")

    def remove_item(self, item):
        if item in self.items_in_cart:
            del self.items_in_cart[item]
            print(item + " was removed")
        else:
            print(item + " is not in the cart")

item = input("What would you like to add to the cart? ")
my_cart = ShoppingCart("Johnny")
my_cart.add_item(item, 3.50)
