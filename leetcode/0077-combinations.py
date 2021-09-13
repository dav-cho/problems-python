##
#### Combinations (medium)
##############################

# Given two integers n and k, return all possible combinations of k numbers out
# of the range [1, n].

# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
 
# Constraints:
# 1 <= n <= 20
# 1 <= k <= n

################################################################################

## backtracking
##############################
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                res.append(curr[:])
            
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
                
        res = []
        backtrack()
        return res


## lexicogrpahic
##############################
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        nums = list(range(1, k + 1)) + [n + 1]
        res, j = [], 0
        while j < k:
            res.append(nums[:k])
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
        
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        #self.assertEqual(solution.combine(4, 2), [[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]])
        #self.assertEqual(solution.combine(1, 1), [[1]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Backtracking
###############################
# Time: O(k * (C_N)^k) - Where (C_N)^k = N! / (N - k)!k! is a number of
#                        combinations to build. append / pop (add / removeLast)
#                        operations are constant-time ones and the only
#                        consuming part here is to append the built combination
#                        of length k to the output
# Space: O((C_N)^k) - To keep all the combinations for an output.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n + 1):
                # add i into the current combination
                curr.append(i)
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        backtrack()
        return output


## Approach 2: Lexicographic (binary sorted) combinations
#############################################################
# Time: O(k (C_N)^k) - Where (C_N)^k = N! / (N−k)!k! is a number of combinations
#                      to build.
# - The external while loop is executed (C_N)^k times since the number of
#   combinations is (C_N)^k. The inner while loop is performed
#   (C_(N - j))^(k - j) times for a given j. In average over (C_N)^k visits from
#   the external loop that results in less than one execution per visit. Hence
#   the most consuming part here is to append each combination of length
#   k((C_N)^k combinations in total) to the output, that takes O(k(C_N)^k) time.
# - You could notice that the second algorithm is much faster than the first one
#   despite they both have the same time complexity. It's a consequence of
#   dealing with the recursive call stack frame for the first algorithm, and the
#   effect is much more pronounced in Python than in Java.

# Space: O((C_N)^k) - To keep all the combinations for an output.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]
        
        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
            
        return output


