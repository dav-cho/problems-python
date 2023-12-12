##
#### 69. Sqrt(x) (easy)
########################################

from math import e, log


## recursion + bit shifts
##############################
# sqrt(x) = 2 * sqrt(x // 4)
# x << y = x * (2**y)
# x >> y = x // (2**y)

# sqrt(x) = sqrt(x >> 2) << 1


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = self.mySqrt(x >> 2) << 1
        right = left + 1

        return left if right * right > x else right


## binary search
##############################
# 0 < sqrt(x) < x/2


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 0, x >> 1

        while left <= right:
            mid = (left + right) >> 1

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = 2
        right = x // 2

        while left <= right:
            num = (left + right) // 2

            if num * num == x:
                return num
            elif num * num < x:
                left = num + 1
            else:
                right = num - 1

        return right


## pocket calculator algorithm
##################################
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left = int(e ** (0.5 * log(x)))
        right = left + 1

        return left if right * right > x else right


## discuss solutions
##############################

## integer newton
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x

        while r * r > x:
            r = (r + x // r) // 2

        return r


class Solution:
    def mySqrt(self, x: int) -> int:
        r = x

        while r * r > x:
            r = (r + x // r) >> 1

        return r


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().mySqrt(4), 2)
        self.assertEqual(Solution().mySqrt(8), 2)


if __name__ == "__main__":
    unittest.main()
