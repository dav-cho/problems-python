##
#### Sum of Two Integers (medium)
#####################################

# Given two integers a and b, return the sum of the two
# integers without using the operators + and -.


# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5

# Constraints:
# -1000 <= a, b <= 1000

#######################################################################

## Approach 1: Bit Manipulation: Easy and Language-Independent
##################################################################
# time: O(1)
# space: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass


## Approach 2: Bit Manipulation: Short Language_Specific Solution
#####################################################################
# time: O(1)
# space: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass


## Tests
############
def test(*args):
    solution = Solution()
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = solution.getSum(test[0], test[1])
            print(f"test {count}")
            print(f"result {count}: {result}")

    return run()


test1 = (1, 2)  # 3
test2 = (2, 3)  # 5

test(test1, test2)


## LeetCode Solutions
#########################


## Approach 1: Bit Manipulation: Easy and Language-Independent
##################################################################
# time: O(1) - each integer contains 32 bits
# space: O(1) - we don't use any additional data structures
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)

        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign


## Shorter:
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1

        return x * sign


## Approach 2: Bit Manipulation: Short Language_Specific Solution
#####################################################################
# time: O(1)
# space: O(1)
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)
