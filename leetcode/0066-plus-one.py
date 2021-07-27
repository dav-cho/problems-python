##
#### Plus One (easy)
########################

# Given a non-empty array of decimal digits representing a non-negative
# integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the
# head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero,
# except the number 0 itself.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

# Example 3:
# Input: digits = [0]
# Output: [1]
 
# Constraints:
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9

################################################################################


class Solution:
    def plus_one(self, digits: list[int]) -> list[int]:
        arr = map(lambda x: str(x), digits)

        return [int(x) for x in str(int(''.join(arr)) + 1)]


class Solution:
    def plus_one(self, digits: list[int]) -> list[int]:
        last = len(digits) - 1

        while digits[last] == 9:
            digits[last] = 0
            last -= 1

            if last < 0:
                return [1] + digits

        digits[last] += 1

        return digits


class Solution:
    def plus_one(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
            
        return [1] + digits


## Tests
############

test1 = [1, 2, 3]       # [1, 2, 4]
test2 = [4, 3, 2, 1]    # [4, 3, 2, 2]
test3 = [0]             # [1]
test4 = [9]          # [1, 0]

solution = Solution()
print(solution.plus_one(test1))
print(solution.plus_one(test2))
print(solution.plus_one(test3))
print(solution.plus_one(test4))


## LeetCode Solutions
#########################

## Approach 1: Schoolbook Addition with Carry
#################################################
# time: O(n) - only one pass
# space: O(n) - although operations are in place, in worst case scenario,
#               we ned to allocate intermediate space to hold the result,
#               which contains n + 1 elements
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
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

