"""
1342. Number of Steps to Reduce a Number to Zero
"""

import unittest


## Naive
########################################################################################
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2:
                num -= 1
            else:
                num //= 2
            count += 1
        return count


## Approach 2: Counting Bits
########################################################################################
# At each step, we either subtract 1 from num, or we divide num by 2. In binary, these
# two operations do something very simple, but very interesting, to a number!

# Recall that odd numbers always have a last bit of 1. Subtracting 1, from an odd
# number, changes the last bit from 1 to 0.

# The bits slid along, and each became the "last" bit. Notice how the 0s took one step
# to remove, and the 1s took two steps to remove.

# This means that we could simply analyze the binary representation of the starting
# num to determine the number of steps needed to reduce it.

# So, to get our answer, we can just add two steps for every 1, and add one step for
# every 0, for each bit in the binary representation.

# There's one thing to be careful of, and that is not inadvertently counting the last
# bit as two steps. The last bit to remove will always be a 1—it was the most
# significant bit in the original num. The algorithm above would add 2 for removing
# this final 1. But actually, when we subtract 1 from it, it goes to zero. So we don't
# need add two steps for this bit. The simplest way of handling this case is to
# subtract 1 from our final steps count, as we know this "off-by-one-error" will always
# happen (except when the initial num is 0, we need to be careful of that
# edge case too!).

# Let's look at another example. The number we'll use is 78; this can be written in
# binary as 1001110. The binary contains four 1s and three 0s, so our total number of
# steps must be (4 * 2) + (3 * 1) - 1 = 10. This the correct result!


class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        for i in bin(num)[2:]:
            count += 1 if i == "0" else 2
        return count - 1


class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = bin(num)[2:]
        return n.count("1") + len(n) - 1


## Approach 3: Counting Bits with Bitwise Operators
########################################################################################
# In Approach 2, we needed to convert the number into a string representation. Strings
# are considerably larger than the integer they represent though. Another way of
# inspecting bits, to check if they're 1 or 0, is to use the bitwise-and (&) operator.

# The result of a & b (a bitwise-and b) looks at each bit in both a and b at the same
# time. If both bits are 1 then bitwise-and sets the same bit of the result to 1, but
# if either are 0 it sets the bit to 0.

# For example, 109 and 57 can be written as 1101101 and 111001 respectively. This image
# shows what happens when we bitwise-and them.

# So, to actually inspect a specific bit, we can use a number that has a 1 followed by
# enough 0s to put the 1 at the position we want it (we commonly call this a "bitmask").
# With this number, we bitwise-and (&) it with the input number. If the input number
# has a 1 at the same position, it'll output 1 at that position, and because all other
# numbers are 0 they will be 0 in the output as well.

# These numbers of the form 1, followed by some number of 0s, are actually just the
# powers of two, where the power is the number of 0s after the one. As such, we can
# check if a bit is a 1 in a number by doing num & (1 << bit) where bit is the bit we
# want to check (0-indexed from the right).

# Just like Approach 2, we look at each bit, and if it's a 1 we add 2 to steps,
# otherwise if it's a 0, we add 1 to steps.

# Algorithm

# Unlike the previous approach, this approach won't work correctly when num = 0 is the
# input. The previous approach did an iteration for the lone 0 bit as it was in the
# string, but for this approach the loop won't run at all. -1 will then be returned
# because of the steps - 1. The solution is to check for num == 0 at the start and
# return 0 if it is detected.


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0

        count = 0
        k = 1
        while k <= num:
            count += 2 if k & num else 1
            k *= 2

        return count - 1


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for input, expected in [
            (14, 6),
            (8, 4),
            (123, 12),
        ]:
            self.assertEqual(Solution().numberOfSteps(input), expected)


if __name__ == "__main__":
    unittest.main()
