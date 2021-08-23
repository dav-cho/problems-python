##
#### Reverse String (easy)
##############################

# Write a function that reverses a string.
# The input string is given as an array of characters s.


# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# Follow up: Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.

#################################################################################


## simple
##############################
class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()


## recursion
##############################
class Solution:
    def reverseString(self, s: list[str]) -> None:
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)
                
        helper(0, len(s) - 1)


## 2 pointers
##############################
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1; right -= 1


class Solution:
    def reverseString(self, s: list[int]) -> None:
        start = 0
        end = len(s) - 1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


## Tests
############
def test(*args):
    solution = Solution()
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            print(f"test {count}")
            solution.reverseString(test)

    return run()


test1 = ["h", "e", "l", "l", "o"]
test2 = ["H", "a", "n", "n", "a", "h"]

test(test1, test2)


## LeetCode Solutions
#########################

## Life is short, use Python
class Solution:
    def reverseString(self, s):
        s.reverse()


## Approach 1: Recursion, In-Place, O(N) Space 
##################################################
# time: O(N) - Time to perform N/2N/2 swaps.
# space: O(N) - To keep the recursion stack
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


## Approach 2: Two Pointers, Iteration, O(1) Space
######################################################
# time: O(N) - To swap N/2 element.
# space: O(1) - It's a constant space solution.
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1

