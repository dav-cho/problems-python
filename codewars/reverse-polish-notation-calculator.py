##
#### Reverse Polish notation calculator (6 kyu)
###################################################

import operator


def calc(expr):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    stack = [0]
    for char in expr.split():
        if char in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[char](a, b))
        else:
            stack.append(float(char))
            
    return stack[-1]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(calc(""), 0, "Should work with empty string")
        self.assertEqual(calc("3"), 3, "Should parse numbers")
        self.assertEqual(calc("3.5"), 3.5, "Should parse float numbers")
        self.assertEqual(calc("1 3 +"), 4, "Should support addition")
        self.assertEqual(calc("1 3 *"), 3, "Should support multiplication")
        self.assertEqual(calc("1 3 -"), -2, "Should support subtraction")
        self.assertEqual(calc("4 2 /"), 2, "Should support division")


if __name__ == '__main__':
    unittest.main()

