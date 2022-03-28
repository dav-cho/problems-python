##
#### 217. Contains Duplicate (easy)
#######################################


## sorting
##############################
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False


## hash set
##############################
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.containsDuplicate([1, 2, 3, 1]), True)
        self.assertEqual(solution.containsDuplicate([1, 2, 3, 4]), False)
        self.assertEqual(
            solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True
        )


if __name__ == "__main__":
    unittest.main()
