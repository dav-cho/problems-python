##
#### Basic Calculator II (medium)
########################################

# Given a string s which represents an expression, evaluate this expression and
# return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
 
# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.

################################################################################

## stack
##############################
class Solution:
    def calculate(self, s: str) -> int:
        operations = '+-*/'
        stack = []
        curr_num = 0
        op = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
                
            if char in operations or i == len(s) - 1:
                if op == '+':
                    stack.append(curr_num)
                if op == '-':
                    stack.append(-curr_num)
                if op == '*':
                    stack.append(stack.pop() * curr_num)
                if op == '/':
                    stack.append(int(stack.pop() / curr_num))
                    
                op = char
                curr_num = 0
                
        res = 0
        
        while stack:
            res += stack.pop()
            
        return res


## no extra space
##############################
class Solution:
    def calculate(self, s: str) -> int:
        operations = '+-*/'
        curr = last = res = 0
        op = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                curr = curr * 10 + int(char)
                
            if char in operations or i == len(s) - 1:
                if op in '+-':
                    res += last
                    
                    if op == '+':
                        last = curr
                    elif op == '-':
                        last = -curr
                
                if op == '*':
                    last *= curr
                elif op == '/':
                    last = int(last / curr)
                    
                op = char
                curr = 0
                
        res += last
        
        return res


## 
##############################
class Solution:
    def calculate(self, s: str) -> int:
        pass


## 
##############################
class Solution:
    def calculate(self, s: str) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.calculate("3+2*2"), 7)
        self.assertEqual(solution.calculate(" 3/2 "), 1)
        self.assertEqual(solution.calculate(" 3+5 / 2 "), 5)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: 
##############################
# Time: 
# Space: 


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


