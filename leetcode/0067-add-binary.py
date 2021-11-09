##
#### Add Binary (easy)
########################################

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
 
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

################################################################################

## built-in methods
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


## 
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass


## 
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            return self.addBinary(b, a)
        
        N = len(a)
        b = b.zfill(N)
        res = 0
        for i in range(N - 1, -1, -1):
            res = (res << 1) + (a[i] + b[i])


## bit by bit
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        N = max(len(a), len(b))
        a, b = a.zfill(N), b.zfill(N)
        
        carry = 0
        res = []
        for i in range(N - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2:
                res.append('1')
            else:
                res.append('0')
            
            carry //= 2
            
        if carry:
            res.append('1')
        
        return ''.join(reversed(res))


## bit manipulation
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = map(lambda x: int(x, 2), (a, b))
        while y:
            res = x ^ y
            carry = (x & y) << 1
            x, y = res, carry
            
        return bin(x)[2:]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().addBinary("11", "1"), "100")
        self.assertEqual(Solution().addBinary("1010", "1011"), "10101")


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Bit-by-Bit Computation
#########################################
# Time: O(max(N, M)) - Where N and M are the lengths of the input strings
#                      a and b.
# Space: O(max(N, M)) - To keep the answer.
class Solution:
    def addBinary(self, a, b) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        
        carry = 0
        answer = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
                
            if carry % 2 == 1:
                answer.append('1')
            else:
                answer.append('0')
            
            carry //= 2
        
        if carry == 1:
            answer.append('1')
        answer.reverse()
        
        return ''.join(answer)


## Approach 2: Bit Manipulation
###################################
# Time: O(N+M) - Where N and M are lengths of the input strings a and b.
# Space: O(max(N, M)) - To keep the answer.

## Implementation
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


## 4-Liner
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]


