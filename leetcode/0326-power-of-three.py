##
#### 326. Power of Three (easy)
########################################


## loop
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            if n % 3:
                return False

            n //= 3

        return n == 1


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        while not n % 3:
            n /= 3

        return n == 1


## recursive
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n % 3:
            return False

        return self.isPowerOfThree(n // 3)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n % 3 != 0:
            return False

        return self.isPowerOfThree(n // 3)


## integer limitations
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pass


## math
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pass


## base conversion
##############################
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().isPowerOfThree(27), True)
        self.assertEqual(Solution().isPowerOfThree(0), False)
        self.assertEqual(Solution().isPowerOfThree(9), True)
        self.assertEqual(Solution().isPowerOfThree(45), False)


if __name__ == "__main__":
    unittest.main()
