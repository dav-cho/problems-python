##
#### 374. Guess Number Higher or Lower (easy)
#################################################


## binary search
##############################
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res > 0:
                left = mid + 1
            else:
                right = mid - 1

        return -1


## ternary search
##############################
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            res1 = guess(mid1)
            res2 = guess(mid2)

            if res1 == 0:
                return mid1
            if res2 == 0:
                return mid2
            elif res1 < 0:
                right = mid1 - 1
            elif res2 > 0:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1

        return -1


## brute force
##############################
class Solution:
    def guessNumber(self, n: int) -> int:
        for num in range(1, n):
            if guess(num) == 0:
                return num

        return n


## first attempt
##############################
class Solution:
    LOWER = -1
    HIGHER = 1
    EQUALS = 0

    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            num = (left + right) // 2
            curr_guess = guess(num)

            if curr_guess == Solution.EQUALS:
                return num
            elif curr_guess == Solution.HIGHER:
                left = num + 1
            else:
                right = num - 1

        return right


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().guessNumber(10), 6)
        self.assertEqual(Solution().guessNumber(1), 1)
        self.assertEqual(Solution().guessNumber(2), 1)


if __name__ == "__main__":
    unittest.main()
