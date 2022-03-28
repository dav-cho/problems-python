##
#### 22. Generate Parentheses (medium)
#########################################


## brute force
##############################
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(curr=[]):
            if len(curr) == 2 * n:
                if valid(curr):
                    res.append("".join(curr))
            else:
                curr.append("(")
                generate(curr)
                curr.pop()
                curr.append(")")
                generate(curr)
                curr.pop()

        def valid(curr):
            balance = 0
            for paren in curr:
                if paren == "(":
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False

            return balance == 0

        res = []
        generate()

        return res


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(x=[]):
            if len(x) == 2 * n:
                if valid(x):
                    res.append("".join(x))
            else:
                x.append("(")
                generate(x)
                x.pop()
                x.append(")")
                generate(x)
                x.pop()

        def valid(x):
            balance = 0
            for c in x:
                if c == "(":
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0

        res = []
        generate()

        return res


## backtracking
##############################
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(curr=[], left=0, right=0):
            if len(curr) == n * 2:
                res.append("".join(curr))
                return

            if left < n:
                curr.append("(")
                backtrack(curr, left + 1, right)
                curr.pop()
            if right < left:
                curr.append(")")
                backtrack(curr, left, right + 1)
                curr.pop()

        res = []
        backtrack()

        return res


## closure number
##############################
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return [""]

        res = []

        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - 1 - i):
                    res.append(f"({left}){right}")

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )
        self.assertEqual(solution.generateParenthesis(1), ["()"])


if __name__ == "__main__":
    unittest.main()
