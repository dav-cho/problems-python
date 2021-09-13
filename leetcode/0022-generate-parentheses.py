##
#### Generate Parentheses
########################################

# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:
# 1 <= n <= 8

################################################################################

## brute force
##############################
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(curr=[]):
            if len(curr) == 2 * n:
                if valid(curr):
                    res.append(''.join(curr))
            else:
                curr.append('(')
                generate(curr)
                curr.pop()
                curr.append(')')
                generate(curr)
                curr.pop()
        
        def valid(curr):
            balance = 0
            for paren in curr:
                if paren == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            
            return balance == 0
        
        res = []
        generate()
        
        return res


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(x=[]):
            if len(x) == 2 * n:
                if valid(x):
                    res.append(''.join(x))
            else:
                x.append('(')
                generate(x)
                x.pop()
                x.append(')')
                generate(x)
                x.pop()
                    
        def valid(x):
            balance = 0
            for c in x:
                if c == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0
        
        res = []
        generate()
        
        return res


## backtracking
##############################
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(curr=[], left=0, right=0):
            if len(curr) == n * 2:
                res.append(''.join(curr))
                return

            if left < n:
                curr.append('(')
                backtrack(curr, left + 1, right)
                curr.pop()
            if right < left:
                curr.append(')')
                backtrack(curr, left, right + 1)
                curr.pop()
                
        res = []
        backtrack()
        
        return res


## closure number
##############################
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return ['']
        
        res = []
        
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - 1 - i):
                    res.append(f"({left}){right}")
                    
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])
        self.assertEqual(solution.generateParenthesis(1), ["()"])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(2^(2n)* n) - For each of 2^(2n) sequences, we need to create and
#                      validate the sequence, which takes O(n) work.
# Space: O(2^(2n)* n) -  Naively, every sequence could be valid. See Approach 3
#                        for development of a tighter asymptotic bound.
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans


## Approach 2: Backtracking
###############################
# Time: O((4^n)/sqrt(n)) - Each valid sequence has at most n steps during
#                       backtracking procedure.
# Space: O((4^n)/sqrt(n)) - As described above, and using O(n) space to store the
#                        sequence.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


## Approach 3: Closure Number
#################################
# Time: O((4^n)/sqrt(n)) - Similar to Approach 2.
# Space: O((4^n)/sqrt(n)) - Similar to Approach 2.
class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


