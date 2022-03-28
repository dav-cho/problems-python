##
#### 8. String to Integer (atoi) (medium)
##########################################


## best?
##############################
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31
        N = len(s)
        sign = 1
        res = 0
        i = 0

        while i < N and s[i] == " ":
            i += 1

        if i < N and s[i] in "+-":
            sign = 1 if s[i] == "+" else -1
            i += 1

        while i < N and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

            if res >= INT_MAX:
                return INT_MAX - 1 if sign == 1 else -INT_MAX

        return res * sign


## first attempt
##############################
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31
        N = len(s)
        sign = 1
        i = 0

        while i < N and s[i] == " ":
            i += 1

        if i < N and s[i] in ["-", "+"]:
            sign = -1 if s[i] == "-" else 1
            i += 1

        res = 0

        while i < N and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

            if res >= INT_MAX and sign == -1:
                return -INT_MAX
            if res >= INT_MAX:
                return INT_MAX - 1
            # if res > INT_MAX / 10 or (res == INT_MAX / 10 and int(s[j]) > 7):
            #    return INT_MAX - 1 if sign == 1 else -INT_MAX

        return res * sign


## Tests
#############

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
