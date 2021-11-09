##
#### Permutations (medium)
##############################

# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]
 
# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

################################################################################

## backtracking
##############################
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        res = []
        
        def backtrack(first=0):
            if first == N:
                res.append(nums[:])
            
            for i in range(first, N):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
            return res
        
        return backtrack()


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
                
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
                
        n = len(nums)
        res = []
        backtrack()
        
        return res

## iterative
##############################
from collections import deque


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        N = len(nums)
        
        if N == 1:
            return [nums]
        if N == 2:
            return [list(nums), list(nums)[::-1]]
        
        nums = deque(nums)
        res = deque()
        
        for _ in range(N):
            num = nums.popleft()
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(num)
                
            res += perms
            nums.append(num)
            
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.permute([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
        self.assertEqual(solution.permute([0,1]), [[0,1],[1,0]])
        self.assertEqual(solution.permute([1]), [[1]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Backtracking
###############################
# Time: O((∑_k=1)^N P(N,k))
# - Where P(N,k) = (N−k)!/N! = N(N−1)...(N−k+1) is so-called
#   k-permutations_of_n, or partial permutation.
# - Here first + 1 = k for the expression simplicity. The formula is easy to
#   understand: for each k (each first) one performs N(N - 1) ... (N - k + 1)
#   operations, and k is going through the range of values from 1 to N (and
#   first from 0 to N - 1).
# - Let's do a rough estimation of the result:
#   N!≤(∑_k=1)^N (N−k)!/N!=(∑_k=1)^N P(N,k)≤N×N!, i.e. the algorithm performs
#   better than O(N×N!) and a bit slower than O(N!).

# Space: O(N!)
# - Since one has to keep N! solutions.

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output


