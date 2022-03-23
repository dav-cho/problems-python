##
#### Delete and Earn (medium)
########################################

# You are given an integer array nums. You want to maximize the number of
# points you get by performing the following operation any number of times:

# - Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must
#   delete every element equal to nums[i] - 1 and every element equal to
#   nums[i] + 1.

# Return the maximum number of points you can earn by applying the above
# operation some number of times.

# Example 1:
# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.

# Example 2:
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.
 
# Constraints:
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 104

################################################################################

from collections import Counter


## reduce to house robber
##############################
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        points = [0] * (max(counts) + 1)
        
        for num in counts:
            points[num] += num * counts[num]
            
        prev = curr = 0
        
        for val in points:
            prev, curr = curr, max(curr, prev + val)
            
        return curr


class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        points = {num: num * counts[num] for num in counts}
        prev = curr = 0
        
        for num in range(max(points) + 1):
            prev, curr = curr, max(curr, prev + points.get(num, 0))
            
        return curr


## dp
##############################
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        counts = Counter(nums)
        prev = None
        avoid = using = 0
        
        for k in sorted(counts):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * counts[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * counts[k] + avoid
                
            prev = k
            
        return max(avoid, using)


## 
##############################
class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().deleteAndEarn([3,4,2]), 6)
        self.assertEqual(Solution().deleteAndEarn([2,2,3,3,3,4]), 9)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Dynamic Programming [Accepted]
#################################################
# Time: 
# Space: 
# Time: O(NlogN) - (Python) Where N is the length of nums. We make a single
#                  pass through the sorted keys of N, and the complexity is
#                  dominated by the sorting step.
# Space: O(N) - (Python) The size of our count.

class Solution(object):
    def deleteAndEarn(self, nums):
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)


