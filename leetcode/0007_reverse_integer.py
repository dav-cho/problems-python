##
#### 7. Reverse Integer (easy)
##################################


## using divmod - best
##############################
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31
        sign = [1, -1][x < 0]
        x = abs(x)
        rev = 0

        while x > 0:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev >= MAX_INT - 1:
                return 0

        return rev * sign


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31
        sign = [1, -1][x < 0]
        x = abs(x)
        rev = 0

        while x > 0:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if not -MAX_INT <= rev < MAX_INT:
                return 0

        return rev * sign


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2**31 / 10
        sign = [1, -1][x < 0]
        x = abs(x)

        rev = 0
        while x != 0:
            if rev > MAX_INT:
                return 0
            x, pop = divmod(x, 10)
            rev = rev * 10 + pop

        return sign * rev


## convert to string (not allowed by problem description)
#############################################################
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev = int(str(abs(x))[::-1])
        if not -(2**31) < rev < (2**31) - 1:
            return 0

        return rev * sign


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rev = int("-" + str(x)[1:][::-1])
        else:
            rev = int(str(x)[::-1])

        if not -(2**31) <= rev <= 2**31:
            return 0

        return rev


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(120), 21)
        self.assertEqual(solution.reverse(0), 0)


if __name__ == "__main__":
    unittest.main()
