##
#### 3Sum (medium)
########################################

# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []
 
# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

################################################################################


## *best: two-pointer
##############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def find_triplet(i):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum < 0:
                    lo += 1
                elif curr_sum > 0:
                    hi -= 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo - 1] == nums[lo]:
                        lo += 1
                        
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                find_triplet(i)
                
        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSumII(i):
            lo = i + 1
            hi = len(nums) - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum < 0:
                    lo += 1
                elif curr_sum > 0:
                    hi -= 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo - 1] == nums[lo]:
                        lo += 1
            
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSumII(i)
                
        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSumII(i):
            lo, hi = i + 1, N - 1
            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]
                if curr_sum < 0:
                    lo += 1
                elif curr_sum > 0:
                    hi -= 1
                else:
                    res.append((nums[i], nums[lo], nums[hi]))
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo - 1] == nums[lo]:
                        lo += 1
                    
        nums.sort()
        N = len(nums)
        res = []
        for i in range(N):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                twoSumII(i)
                
        return res


## two-pointer
##############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
                
        return res
    
    def twoSumII(self, nums, i, res):
        lo = i + 1
        hi = len(nums) - 1
        while lo < hi:
            curr_sum = nums[i] + nums[lo] + nums[hi]
            if curr_sum < 0:
                lo += 1
            elif curr_sum > 0:
                hi -= 1
            else:
                res.append((nums[i], nums[lo], nums[hi]))
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
                
        return res
    
    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            curr_sum = nums[i] + nums[lo] + nums[hi]
            if curr_sum < 0:
                lo += 1
            elif curr_sum > 0:
                hi -= 1
            else:
                res.append((nums[i], nums[lo], nums[hi]))
                lo += 1
                hi -= 1
                while lo < hi and nums[lo - 1] == nums[lo]:
                    lo += 1


## no-sort
##############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        dups = set()
        seen = {}
        for i, x in enumerate(nums):
            if x not in dups:
                dups.add(x)
                for j, y in enumerate(nums[i + 1:]):
                    comp = -x - y
                    if comp in seen and seen[comp] == i:
                        res.add(tuple(sorted((x, y, comp))))
                    seen[y] = i
                    
        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        dups = set()
        seen = {}
        for i, x in enumerate(nums):
            if x not in dups:
                dups.add(x)
                for j, y in enumerate(nums[i + 1:]):
                    comp = -x - y
                    if comp in seen and seen[comp] == i:
                        res.add(tuple(sorted([x, y, comp])))
                    seen[y] = i
                    
        return res


## hashset
##############################
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
                
        return res
    
    def twoSum(self, nums, i, res):
        seen = set()
        j = i + 1
        while j < len(nums):
            comp = -nums[i] - nums[j]
            if comp in seen:
                res.append((nums[i], nums[j], comp))
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(Solution().threeSum([-1,0,1,2,-1,-4]), [(-1,-1,2),(-1,0,1)])
        self.assertCountEqual(Solution().threeSum([]), [])
        self.assertCountEqual(Solution().threeSum([0]), [])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Two Pointers
##############################
# Time: O(n^2) - twoSumII is O(n), and we call it n times.
# - Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n^2).
#   This is asymptotically equivalent to O(n^2).

# Space: from O(logn) to O(n)
# - Depending on the implementation of the sorting algorithm. For the purpose
#   of complexity analysis, we ignore the memory required for the output.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1


## Approach 2: Hashset
##############################
# Time: O(n^2) - twoSum is O(n), and we call it n times.
# - Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n^2).
#   This is asymptotically equivalent to O(n^2).

# Space: O(n)
# - For the hashset.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1


## Approach 3: "No-Sort"
##############################
# Time: 
# Space: 
# Time: O(n 2) - We have outer and inner loops, each going through n elements.
# - While the asymptotic complexity is the same, this algorithm is noticeably
#   slower than the previous approach. Lookups in a hashset, though requiring a
#   constant time, are expensive compared to the direct memory access.

# Space: O(n) - For the hashset/hashmap.
# - For the purpose of complexity analysis, we ignore the memory required for
#   the output. However, in this approach we also store output in the hashset
#   for deduplication. In the worst case, there could be O(n^2) triplets in the
#   output, like for this example: [-k, -k + 1, ..., -1, 0, 1, ... k - 1, k].
#   Adding a new number to this sequence will produce n / 3 new triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res


