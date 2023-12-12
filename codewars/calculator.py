##
#### Calculator (3 kyu)
###################################################

from collections import deque
import operator


class Calculator(object):
    def evaluate(self, string):
        #operations = {
        #    '+': lambda a, b: a + b,
        #    '-': lambda a, b: a - b,
        #    '*': lambda a, b: a * b,
        #    '/': lambda a, b: a // b,
        #}
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
        }
        
        if len(string) == 1:
            return int(string)
        
        arr = string.split()
        stack = []
        i = 0

        while i < len(arr):
            if arr[i] == '(':
                parens = [arr[i]]
                j = i + 1

                while parens:
                    if arr[j] == '(':
                        parens.append(arr[j])
                    if arr[j] == ')':
                        parens.pop()
                    j += 1

                stack.append(str(self.evaluate(' '.join(arr[i + 1:j - 1]))))
                i = j - 1

            else:
                stack.append(arr[i])

            i += 1

        def helper(operators):
            k = 1

            while k < len(stack) - 1:
                if stack[k] in operators:
                    op = operations[stack[k]]
                    a = int(stack[k - 1])
                    b = int(stack[k + 1])

                    stack[k - 1] = str(op(a, b))
                    stack.pop(k)
                    stack.pop(k)
                    continue

                k += 1

        helper('*/')
        helper('+-')

        return int(stack[0])



## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
        self.assertEqual(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
        self.assertEqual(Calculator().evaluate('1 + 1'), 2)
        self.assertEqual(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
        self.assertEqual(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
        self.assertEqual(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
        self.assertEqual(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)

        #self.assertEqual(Calculator().evaluate("44 / 22 + ((30 + 5)) * 4 - 62"), 80)


if __name__ == '__main__':
    unittest.main()

