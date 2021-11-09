##
#### Missing Number (easy)
########################################

# Given an array nums containing n distinct numbers in the range [0, n], return
# the only number in the range that is missing from the array.

# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range
#              [0,3]. 2 is the missing number in the range since it does not
#              appear in nums.

# Example 2:
# input: nums = [0,1]
# output: 2
# explanation: n = 2 since there are 2 numbers, so all numbers are in the range
#              [0,2]. 2 is the missing number in the range since it does not
#              appear in nums.

# Example 3:
# input: nums = [9,6,4,2,3,5,7,0,1]
# output: 8
# explanation: n = 9 since there are 9 numbers, so all numbers are in the range
#              [0,9]. 8 is the missing number in the range since it does not
#              appear in nums.

# Example 4:
# input: nums = [0]
# output: 1
# explanation: n = 1 since there is 1 number, so all numbers are in the range
#              [0,1]. 1 is the missing number in the range since it does not
#              appear in nums.
 
# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# all the numbers of nums are unique.

# Follow Up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

################################################################################


## best*
##############################

## gauss' formula
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        expected = N * (N + 1) // 2
        actual = sum(nums)
        
        return expected - actual


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(set(nums))


## bit manipulation
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        
        for i, num in enumerate(nums):
            res ^= i ^ num
            
        return res


## hash set
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        seen = set(nums)
        
        for num in range(len(nums) + 1):
            if num not in seen:
                return num


## bit manipulation
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        
        for i, num in enumerate(nums):
            res ^= i ^ num
            
        return res


## sorting
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        
        for i, num in enumerate(nums):
            if i != num:
                return i
            
        return nums[-1] +  1


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        
        for i in range(1, len(nums)):
            expected = nums[i - 1] + 1
            
            if nums[i] != expected:
                return expected


## gauss' formula
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        expected = N * (N + 1) // 2
        actual = sum(nums)
        
        return expected - actual


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        expected_sum = N * (N + 1) // 2
        actual_sum = sum(nums)
        
        return expected_sum - actual_sum


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        N = len(nums)
        
        return (N * (N + 1) // 2) - sum(nums)


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        expected = len(nums) * (len(nums) + 1) // 2
        actual = sum(nums)
        
        return expected - actual


## first attempt
##############################
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        mx = max(nums)
        seen = set(nums)
        
        for num in range(mx):
            if num not in seen:
                return num
            
        return mx + 1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().missingNumber([9,6,4,2,3,5,7,0,1]), 8)
        self.assertEqual(Solution().missingNumber([0]), 1)

if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Sorting [Accepted]
#####################################
# Time: O(nlogn)
# - The only elements of the algorithm that have asymptotically nonconstant
#   time complexity are the main for loop (which runs in O(n) time), and the
#   sort invocation (which runs in O(nlogn) time for Python and Java).
#   Therefore, the runtime is dominated by sort, and the entire runtime is
#   O(nlogn).

# Space: O(1) or O(n)
# - In the sample code, we sorted nums in place, allowing us to avoid allocating
#   additional space. If modifying nums is forbidden, we can allocate an O(n)
#   size copy and sort that instead.

class Solution:
    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num


## Approach 2: HashSet [Accepted]
#####################################
# Time: O(n)
# - Because the set allows for O(1) containment queries, the main loop runs in
#   O(n) time. Creating num_set costs O(n) time, as each set insertion runs in
#   amortized O(1) time, so the overall runtime is O(n+n)=O(n).

# Space: O(n)
# - nums contains n−1 distinct elements, so it costs O(n) space to store a set
#   containing all of them.

class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


## Approach 3: Bit Manipulation [Accepted]
##############################################
# Time: O(n) - Assuming that XOR is a constant-time operation, this algorithm
#              does constant work on nn iterations, so the runtime is overall
#              linear.
# Space: O(1) - This algorithm allocates only constant additional space.
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


## Approach 4: Gauss' Formula [Accepted]
############################################
# Time: O(n)
# - Although Gauss' formula can be computed in O(1) time, summing nums costs us
#   O(n) time, so the algorithm is overall linear. Because we have no
#   information about which number is missing, an adversary could always design
#   an input for which any algorithm that examines fewer than n numbers fails.
#   Therefore, this solution is asymptotically optimal.

# Space: O(1)
# - This approach only pushes a few integers around, so it has constant memory
#   usage.

class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


