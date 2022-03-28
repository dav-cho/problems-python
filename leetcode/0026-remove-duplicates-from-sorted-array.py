##
#### 26. Remove Duplicates from Sorted Array (easy)
#######################################################


## two pointers
##############################
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.removeDuplicates([1, 1, 2]), 2)
        # nums = [1,2,_]
        self.assertEqual(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
        # nums = [0,1,2,3,4,_,_,_,_,_]


if __name__ == "__main__":
    unittest.main()
