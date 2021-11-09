##
#### Roman to Integer (easy)
########################################

# Roman numerals are represented by seven different symbols:
# I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added
# together. 12 is written as XII, which is simply X + II. The number 27 is
# written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is
# written as IV. Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX. There
# are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3

# Example 2:
# Input: s = "IV"
# Output: 4

# Example 3:
# Input: s = "IX"
# Output: 9

# Example 4:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 5:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

################################################################################

## right to left pass
##############################
class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        res = vals[s[-1]]
        
        for i in range(len(s) - 2, -1, -1):
            if vals[s[i]] < vals[s[i + 1]]:
                res -= vals[s[i]]
            else:
                res += vals[s[i]]
                
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        res = vals.get(s[-1])
        
        for i in reversed(range(len(s) - 1)):
            if vals[s[i]] < vals[s[i + 1]]:
                res -= vals[s[i]]
            else:
                res += vals[s[i]]
                
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        res = 0
        prev = 0
        
        for i in range(len(s) - 1, -1, -1):
            if vals[s[i]] < prev:
                res -= vals[s[i]]
            else:
                res += vals[s[i]]
                
            prev = vals[s[i]]
                
        return res


## left to right pass
##############################
class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        N = len(s)
        res = 0
        i = 0
        
        while i < N:
            if i < N - 1 and vals[s[i]] < vals[s[i + 1]]:
                res += vals[s[i + 1]] - vals[s[i]]
                i += 2
            else:
                res += vals[s[i]]
                i += 1
                
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        N = len(s)
        res = 0
        i = 0
        
        while i < N:
            if i + 1 < N and vals[s[i]] < vals[s[i + 1]]:
                res += vals[s[i + 1]] - vals[s[i]]
                i += 2
            else:
                res += vals[s[i]]
                i += 1
                
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        res = 0
        i = 0
        
        while i < len(s):
            if i + 1 < len(s) and vals[s[i]] < vals[s[i + 1]]:
                res += vals[s[i + 1]] - vals[s[i]]
                i += 2
            else:
                res += vals[s[i]]
                i += 1
                
        return res


## left to right pass improved
##################################
class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40, 
            "XC": 90,
            "CD": 400,
            "CM": 900
        }        

        N = len(s)
        res = 0
        i = 0
        
        while i < N:
            if i < N - 1 and s[i:i + 2] in vals:
                res += vals[s[i:i + 2]]
                i += 2
            else:
                res += vals[s[i]]
                i += 1
                
        return res


class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40, 
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        res = 0
        i = 0
        
        while i < len(s):
            if i < len(s) - 1 and s[i:i + 2] in vals:
                res += vals[s[i:i + 2]]
                i += 2
            else:
                res += vals[s[i]]
                i += 1
                
        return res


## 
##############################
class Solution:
    def romanToInt(self, s: str) -> int:
        pass


## 
##############################
class Solution:
    def romanToInt(self, s: str) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Left-to-Right Pass
#####################################
# Time: O(1) - Let nn be the length of the input string
#              (the total number of symbols in it).
# - As there is a finite set of roman numerals, the maximum number possible
#   number can be 3999, which in roman numerals is MMMCMXCIX. As such the time
#   complexity is O(1).
# - If roman numerals had an arbitrary number of symbols, then the time
#   complexity would be proportional to the length of the input, i.e. O(n).
#   This is assuming that looking up the value of each symbol is O(1).

# Space: O(1)
# - Because only a constant number of single-value variables are used, the
#   space complexity is O(1).

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += values[s[i]]
                i += 1
        return total


## Approach 2: Left-to-Right Pass Improved
##############################################
# Time: O(1) - Same as Approach 1.
# Space: O(1) - Same as Approach 1.

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "IV": 4,
    "IX": 9,
    "XL": 40, 
    "XC": 90,
    "CD": 400,
    "CM": 900
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            # This is the subtractive case.
            if i < len(s) - 1 and s[i:i+2] in values:
                total += values[s[i:i+2]] 
                i += 2
            else:
                total += values[s[i]]
                i += 1
        return total


## Approach 3: Right-to-Left Pass
#####################################
# Time: O(1) - Same as Approach 1.
# Space: O(1) - Same as Approach 1.

values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = values.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total



