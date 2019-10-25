"""
Create a function that determines whether a
shopping order is eligible for free shipping.
An order is eligible for free shipping if the
total cost of items purchased exceeds $50.00.

Examples
free_shipping({ "Shampoo": 5.99, "Rubber Ducks": 15.99 }) ➞ False
free_shipping({ "Flatscreen TV": 399.99 }) ➞ True
free_shipping({ "Monopoly": 11.99, "Secret Hitler": 35.99, "Bananagrams": 13.99 }) ➞ True

Notes
Ignore tax or additional fees when calculating the total order cost.

"""

# my solution
def free_shipping(order):
    total_sum = 0
    for value in order.values():
        total_sum += value
    if total_sum > 50:
        return True
    else:
        return False


# function test
free_shipping({ "Shampoo": 5.99, "Rubber Ducks": 15.99 })
