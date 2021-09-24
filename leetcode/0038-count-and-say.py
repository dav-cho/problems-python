##
#### Count and Say (medium)
########################################

# The count-and-say sequence is a sequence of digit strings defined by the
# recursive formula:

# - countAndSay(1) = "1"
# - countAndSay(n) is the way you would "say" the digit string from
#   countAndSay(n-1), which is then converted into a different digit string.

# To determine how you "say" a digit string, split it into the minimal number of
# groups so that each group is a contiguous section all of the same character.
# Then for each group, say the number of characters, then say the character. To
# convert the saying into a digit string, replace the counts with a number and
# concatenate every saying.

# For example, the saying and conversion for digit string "3322251":

# - "3322251"
# - two 3's, three 2's, one 5 and one 1
# - 2 3 + 3 2 + 1 5 + 1 1
# - "23321511"

# Given a positive integer n, return the nth term of the count-and-say sequence.

# Example 1:
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.

# Example 2:
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

# Constraints:
# 1 <= n <= 30

################################################################################

## first attempt
##############################
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        
        for _ in range(n - 1):
            char = res[0]
            count = 1
            curr = ''
            
            for i in range(1, len(res)):
                if res[i] == char:
                    count += 1
                else:
                    curr += str(count) + char
                    char = res[i]
                    count = 1
                    
            res = curr + str(count) + char
            
        return res


class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        
        for _ in range(n - 1):
            char = res[0]
            count = 1
            curr = ''
            
            for i in range(1, len(res)):
                if res[i] == char:
                    count += 1
                else:
                    curr += str(count) + char
                    char = res[i]
                    count = 1
            
            res = curr + str(count) + char
            
        return res


## 
##############################
class Solution:
    def countAndSay(self, n: int) -> str:
        pass


## 
##############################
class Solution:
    def countAndSay(self, n: int) -> str:
        pass


## 
##############################
class Solution:
    def countAndSay(self, n: int) -> str:
        pass


## 
##############################
class Solution:
    def countAndSay(self, n: int) -> str:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(1), "1")
        self.assertEqual(solution.countAndSay(4), "1211")
        self.assertEqual(solution.countAndSay(5), "111221")


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


