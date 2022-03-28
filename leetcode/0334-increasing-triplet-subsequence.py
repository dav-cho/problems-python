##
#### 334. Increasing Triplet Subsequence (medium)
#####################################################


## linear search
##############################
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first_num = float("inf")
        second_num = float("inf")
        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True

        return False


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().increasingTriplet([1, 2, 3, 4, 5]), True)
        self.assertEqual(Solution().increasingTriplet([5, 4, 3, 2, 1]), False)
        self.assertEqual(Solution().increasingTriplet([2, 1, 5, 0, 4, 6]), True)


if __name__ == "__main__":
    unittest.main()
