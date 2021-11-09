##
#### Valid Parentheses (easy)
#################################

# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([)]"
# Output: false

# Example 5:
# Input: s = "{[]}"
# Output: true

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

################################################################################


## stack
##############################
class Solution:
    def isValid(self, s: str) -> bool:
        table = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            if char in table:
                if stack and stack[-1] == table[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return not stack


## first attempt
##############################
class Solution:
    def isValid(self, s: str) -> bool:
        table = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            if char in table:
                if stack and stack[-1] == table[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return not stack


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().isValid("()"), True)
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("(]"), False)
        self.assertEqual(Solution().isValid("([)]"), False)
        self.assertEqual(Solution().isValid("{[]}"), True)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Stacks
##############################
# Time: O(n) - Because we simply traverse the given string one character at a
#              time and push and pop operations on a stack take O(1) time.
# Space: O(n) - As we push all opening brackets onto the stack and in the worst
#               case, we will end up pushing all the brackets onto the stack.
#               e.g. ((((((((((.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


