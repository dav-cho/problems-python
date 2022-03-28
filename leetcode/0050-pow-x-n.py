##
#### 50. Pow(x, n) (medium)
###############################


## fast power recursive
##############################
# if n is even: (x**n)**2 = x**(2*n) -> x**n = A * A
# if x is odd: x**(n-1) = A * A -> x**n = A * A * x


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        return self.fast_pow(x, n)

    def fast_pow(self, x, n):
        if n == 0:
            return 1

        half = self.fast_pow(x, n >> 1)

        if n % 2 == 0:
            return half * half

        return half * half * x


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        return self.fast_pow(x, n)

    def fast_pow(self, x, n):
        if n == 0:
            return 1

        half = self.fast_pow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


## fast power iterative
##############################
# x**(a+b) = x**a + x**b
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        curr_product = x
        i = n

        while i > 0:
            if i % 2 == 1:
                res *= curr_product

            curr_product *= curr_product
            i >>= 1

        return res


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        curr_product = x
        i = n
        while i > 0:
            if i % 2 == 1:
                ans *= curr_product
            curr_product *= curr_product
            i //= 2

        return ans


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x **= 2
            # x *= x
            n //= 2

        return ans


## brute force (TLE)
##############################
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1

        for _ in range(n):
            res *= x

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.myPow(2.00000, 10), 1024.00000)
        self.assertEqual(solution.myPow(2.10000, 3), 9.26100)
        self.assertEqual(solution.myPow(2.00000, -2), 0.25000)


if __name__ == "__main__":
    unittest.main()
