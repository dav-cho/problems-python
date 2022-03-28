##
#### 227. Basic Calculator II (medium)
###########################################


## stack
##############################
class Solution:
    def calculate(self, s: str) -> int:
        operations = "+-*/"
        stack = []
        curr_num = 0
        op = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)

            if char in operations or i == len(s) - 1:
                if op == "+":
                    stack.append(curr_num)
                if op == "-":
                    stack.append(-curr_num)
                if op == "*":
                    stack.append(stack.pop() * curr_num)
                if op == "/":
                    stack.append(int(stack.pop() / curr_num))

                op = char
                curr_num = 0

        res = 0

        while stack:
            res += stack.pop()

        return res


## no extra space
##############################
class Solution:
    def calculate(self, s: str) -> int:
        operations = "+-*/"
        curr = last = res = 0
        op = "+"

        for i, char in enumerate(s):
            if char.isdigit():
                curr = curr * 10 + int(char)

            if char in operations or i == len(s) - 1:
                if op in "+-":
                    res += last

                    if op == "+":
                        last = curr
                    elif op == "-":
                        last = -curr

                if op == "*":
                    last *= curr
                elif op == "/":
                    last = int(last / curr)

                op = char
                curr = 0

        res += last

        return res


##
##############################
class Solution:
    def calculate(self, s: str) -> int:
        pass


##
##############################
class Solution:
    def calculate(self, s: str) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.calculate("3+2*2"), 7)
        self.assertEqual(solution.calculate(" 3/2 "), 1)
        self.assertEqual(solution.calculate(" 3+5 / 2 "), 5)


if __name__ == "__main__":
    unittest.main()
