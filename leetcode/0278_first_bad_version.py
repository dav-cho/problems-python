##
#### 278. First Bad Version (easy)
########################################


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


## binary search / divide and conquer
#########################################
class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return right


class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.firstBadVersion(5), 4)
        self.assertEqual(solution.firstBadVersion(1), 1)


if __name__ == "__main__":
    unittest.main()
