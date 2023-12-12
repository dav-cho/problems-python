##
#### 367. Valid Perfect Square (easy)
#########################################


## newton's method
##############################
# x = (x + num/x) / 2
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        x = num >> 1

        while x * x > num:
            x = (x + num // x) >> 1

        return x * x == num


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        x = num // 2

        while x * x > num:
            x = (x + num // x) // 2

        return x * x == num


## binary search
##############################
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num >> 1

        while left <= right:
            mid = (left + right) >> 1

            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1

        return False


## first attempt
##############################
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def get_sqrt(x):
            if x < 2:
                return x

            left = get_sqrt(x >> 2) << 1
            right = left + 1

            return left if right * right > x else right

        res = get_sqrt(num)

        return res * res == num


##
##############################
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().isPerfectSquare(16), True)
        self.assertEqual(Solution().isPerfectSquare(14), False)


if __name__ == "__main__":
    unittest.main()
