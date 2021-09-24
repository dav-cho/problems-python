##
#### Plus One (easy)
########################################

# You are given a large integer represented as an integer array digits, where
# each digits[i] is the ith digit of the integer. The digits are ordered from
# most significant to least significant in left-to-right order. The large
# integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [0]
# Output: [1]
# Explanation: The array represents the integer 0.
# Incrementing by one gives 0 + 1 = 1.
# Thus, the result should be [1].

# Example 4:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 
# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

################################################################################

## attempt 1
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        carry = 0
        
        for i in range(len(digits) - 1, -1, -1):
            carry, new_digit = divmod(digits[i] + carry, 10)
            digits[i] = new_digit
            
        return [carry] + digits if carry else digits


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        remainder = 0
        
        for i in range(len(digits) - 1, -1, -1):
            new_digit = digits[i] + remainder
            remainder, new_digit = divmod(new_digit, 10)
            digits[i] = new_digit
            
        if remainder:
            digits.insert(0, remainder)
            
        return digits


## 
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        pass


## 
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        pass


## 
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        carry = 0
        
        for i in range(len(digits) - 1, -1, -1):
            carry, digit = divmod(digits[i] + carry, 10)
            digits[i] = digit
            
            
        return [carry] + digits if carry else digits


## recursive
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 0:
            return [1]

        if digits[-1] != 9:
            return digits[:-1] + [digits[-1] + 1]

        return self.plusOne(digits[:-1]) + [0]


## recursive (not working)
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
        else:
            digits[-1] += 1

        return digits


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(solution.plusOne([4,3,2,1]), [4,3,2,2])
        self.assertEqual(solution.plusOne([0]), [1])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Schoolbook Addition with Carry
#################################################
# Let N be the number of elements in the input list.

# Time: O(N)
# - Since it's not more than one pass along the input list.

# Space: O(N)
# - Although we perform the operation in-place (i.e. on the input list itself),
#   in the worst case scenario, we would need to allocate an intermediate space
#   to hold the result, which contains the N + 1 elements. Hence the overall
#   space complexity of the algorithm is O(N).

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits


