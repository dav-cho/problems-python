"""
8. String to Integer (atoi) (medium)
"""


## Follow the Rules
########################################################################################


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = (2**31) - 1
        INT_MIN = -(2**31)

        n = len(s)
        res = 0
        sign = 1
        i = 0

        while i < n and s[i] == " ":
            i += 1

        if i < n and s[i] in ("+", "-"):
            sign = 1 if s[i] == "+" else -1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])

            if (res > INT_MAX // 10) or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            res = res * 10 + digit
            i += 1

        return res * sign


## Tests
########################################################################################


import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.myAtoi("42"), 42)
        self.assertEqual(solution.myAtoi("   -42"), -42)
        self.assertEqual(solution.myAtoi("4193 with words"), 4193)
        self.assertEqual(solution.myAtoi("words and 987"), 0)
        self.assertEqual(solution.myAtoi("-91283472332"), -2147483648)
        self.assertEqual(solution.myAtoi("-2147483648"), -2147483648)


if __name__ == "__main__":
    unittest.main()
