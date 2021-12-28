##
#### Missing Ranges (easy)
########################################

# You are given an inclusive range [lower, upper] and a sorted unique integer
# array nums, where all elements are in the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is
# not in nums.

# Return the smallest sorted list of ranges that cover every missing number
# exactly. That is, no element of nums is in any of the ranges, and each
# missing number is in one of the ranges.

# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b
#
# Example 1:
# Input: nums = [0,1,3,50,75], lower = 0, upper = 99
# Output: ["2","4->49","51->74","76->99"]
# Explanation: The ranges are:
# [2,2] --> "2"
# [4,49] --> "4->49"
# [51,74] --> "51->74"
# [76,99] --> "76->99"

# Example 2:
# Input: nums = [], lower = 1, upper = 1
# Output: ["1"]
# Explanation: The only missing range is [1,1], which becomes "1".

# Example 3:
# Input: nums = [], lower = -3, upper = -1
# Output: ["-3->-1"]
# Explanation: The only missing range is [-3,-1], which becomes "-3->-1".

# Example 4:
# Input: nums = [-1], lower = -1, upper = -1
# Output: []
# Explanation: There are no missing ranges since there are no missing numbers.

# Example 5:
# Input: nums = [-1], lower = -2, upper = -1
# Output: ["-2"]
 
# Constraints:
# -109 <= lower <= upper <= 109
# 0 <= nums.length <= 100
# lower <= nums[i] <= upper
# All the values of nums are unique.

################################################################################


## linear scan
##############################
class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        res = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 < curr - 1:
                res.append(f'{prev + 1}->{curr - 1}')
            elif prev + 1 == curr - 1:
                res.append(str(prev + 1))
            prev = curr
                
        return res


class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        def format_range(lower, upper):
            if lower == upper:
                return str(lower)
            return f'{lower}->{upper}'
        
        res = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                res.append(format_range(prev + 1, curr - 1))
            prev = curr
        
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findMissingRanges([0,1,3,50,75], 0, 99), ["2","4->49","51->74","76->99"])
        self.assertEqual(Solution().findMissingRanges([], 1, 1), ["1"])
        self.assertEqual(Solution().findMissingRanges([], -3, -1), ["-3->-1"])
        self.assertEqual(Solution().findMissingRanges([-1], -1, -1), [])
        self.assertEqual(Solution().findMissingRanges([-1], -2, -1), ["-2"])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Linear Scan
##############################
# Time: O(N)
# - This is because we are only iterating over the array once, and at each
#   step, we're performing O(1) operations. We treat the string building as
#   O(1) because the strings can never be more than a fixed size.
# Space: 
# - The output list has a worst case size of O(N). This case occurs when we
#   have a missing range between each of the consecutive elements in the input
#   array (for example, if the input array contains all even numbers between
#   lower and upper). We aren't using any other additional space, beyond
#   fixed-sized constants that don't grow with the size of the input.
# - However, output space that is simply used to return the output (and not to
#   do any processing) is not counted for the purpose of space complexity
#   analysis. For this reason, the overall space complexity is O(1).
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # formats range in the requested format
        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" + str(upper)

        result = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                result.append(formatRange(prev + 1, curr - 1))
            prev = curr
        return result


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


