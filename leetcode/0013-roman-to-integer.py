##
#### 13. Roman to Integer (easy)
########################################


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


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()

