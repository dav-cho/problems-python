##
#### Calculating with Functions (5 kyu)
###########################################

def expression(num, operation):
    if operation:
        return operation(num)
    return num

def zero(operation=None):
    return expression(0, operation)
def one(operation=None):
    return expression(1, operation)
def two(operation=None):
    return expression(2, operation)
def three(operation=None):
    return expression(3, operation)
def four(operation=None):
    return expression(4, operation)
def five(operation=None):
    return expression(5, operation)
def six(operation=None):
    return expression(6, operation)
def seven(operation=None):
    return expression(7, operation)
def eight(operation=None):
    return expression(8, operation)
def nine(operation=None):
    return expression(9, operation)

def plus(b):
    return lambda a: a + b
def minus(b):
    return lambda a: a - b
def times(b):
    return lambda a: a * b
def divided_by(b):
    return lambda a: a // b


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)


if __name__ == '__main__':
    unittest.main()

