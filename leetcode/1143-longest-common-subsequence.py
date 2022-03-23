##
#### Longest Common Subsequence (medium)
############################################

# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.

# - For example, "ace" is a subsequence of "abcde".

# A common subsequence of two strings is a subsequence that is common to both
# strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 
# Constraints:
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

################################################################################

from functools import lru_cache


## bottom-up dp space optimized
###################################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if m > n:
            return self.longestCommonSubsequence(text2, text1)
        
        prev = [0] * (m + 1)
        for col in reversed(range(n)):
            curr = [0] * (m + 1)
            for row in reversed(range(m)):
                if text1[row] == text2[col]:
                    curr[row] = 1 + prev[row + 1]
                else:
                    curr[row] = max(curr[row + 1], prev[row])
                    
            prev = curr
            
        return prev[0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        if rows > cols:
            return self.longestCommonSubsequence(text2, text1)
        
        prev = [0] * (rows + 1)
        for col in reversed(range(cols)):
            curr = [0] * (rows + 1)
            for row in reversed(range(rows)):
                if text1[row] == text2[col]:
                    below_right = prev[row + 1]
                    curr[row] = 1 + below_right
                else:
                    below = curr[row + 1]
                    right = prev[row]
                    curr[row] = max(below, right)
                    
            prev = curr
            
        return prev[0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        if n > m:
            text1, text2 = text2, text1
            n, m = m, n
            
        prev = [0] * (n + 1)
        
        for col in range(m - 1, -1, -1):
            curr = [0] * (n + 1)
            
            for row in range(n - 1, -1, -1):
                if text1[row] == text2[col]:
                    curr[row] = 1 + prev[row + 1]
                else:
                    curr[row] = max(prev[row], curr[row + 1])
                    
            prev = curr
            
        return prev[0]


## bottom-up dp
##############################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        memo = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if text1[row] == text2[col]:
                    below_right = memo[row + 1][col + 1]
                    memo[row][col] = 1 + below_right
                else:
                    below = memo[row + 1][col]
                    right = memo[row][col + 1]
                    memo[row][col] = max(below, right)
                    
        return memo[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        if rows > cols:
            return self.longestCommonSubsequence(text2, text1)
        
        for char1 in reversed(range(rows)):
            for char2 in reversed(range(cols)):
                if text1[char1] == text2[char2]:
                    dp[char1][char2] = 1 + dp[char1 + 1][char2 + 1]
                else:
                    dp[char1][char2] = max(dp[char1 + 1][char2], dp[char1][char2 + 1])
                    
        return dp[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        memo = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if text1[row] == text2[col]:
                    memo[row][col] = 1 + memo[row + 1][col + 1]
                else:
                    memo[row][col] = max(memo[row + 1][col], memo[row][col + 1])
                    
        return memo[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        
        for col in reversed(range(n)):
            for row in reversed(range(m)):
                if text1[row] == text2[col]:
                    memo[row][col] = 1 + memo[row + 1][col + 1]
                else:
                    memo[row][col] = max(memo[row + 1][col], memo[row][col + 1])
                    
        return memo[0][0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for col in reversed(range(m)):
            for row in reversed(range(n)):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
                    
        return dp[0][0]


## improved top-down memoization
####################################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + dp(p1 + 1, p2 + 1)
            
            return max(dp(p1, p2 + 1), dp(p1 + 1, p2))
        
        return dp(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            if text1[p1] == text2[p2]:
                return 1 + dp(p1 + 1, p2 + 1)
            
            option1 = dp(p1, p2 + 1)
            option2 = dp(p1 + 1, p2)
            
            return max(option1, option2)
        
        return dp(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            
            if text1[p1] == text2[p2]:
                memo[(p1, p2)] = 1 + dp(p1 + 1, p2 + 1)
            else:
                memo[(p1, p2)] = max(dp(p1, p2 + 1), dp(p1 + 1, p2))
            
            return memo[(p1, p2)]
        
        return dp(0, 0)


## top-down memoization
##############################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(maxsize=None)
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            option1 = dp(p1 + 1, p2)
            option2 = 0
            first = text2.find(text1[p1], p2)
            
            if first != -1:
                option2 = 1 + dp(p1 + 1, first + 1)
                
            return max(option1, option2)
        
        return dp(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            
            option_1 = dp(p1 + 1, p2)
            
            option_2 = 0
            first = text2.find(text1[p1], p2)
            
            if first != -1:
                option_2 = 1 + dp(p1 + 1, first + 1)
                
            memo[(p1, p2)] = max(option_1, option_2)
            
            return memo[(p1, p2)]
        
        return dp(0, 0)


## 
##############################
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().longestCommonSubsequence("abcde", "ace"), 3)  
        self.assertEqual(Solution().longestCommonSubsequence("abc", "abc"), 3)
        self.assertEqual(Solution().longestCommonSubsequence("abc", "def"), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Memoization
##############################
# Time: O(M ⋅ N^2)
# - We analyze a memoized-recursive function by looking at how many unique
#   subproblems it will solve, and then what the cost of solving each
#   subproblem is.
# - The input parameters to the recursive function are a pair of integers;
#   representing a position in each string. There are M possible positions for
#   the first string, and N for the second string. Therefore, this gives us
#   M ⋅ N possible pairs of integers, and is the number of subproblems to be
#   solved.
# - Solving each subproblem requires, in the worst case, an O(N) operation;
#   searching for a character in a string of length N. This gives us a total
#   of (M ⋅ N^2).

# Space: O(M ⋅ N)
# - We need to store the answer for each of the M ⋅ N subproblems. Each
#   subproblem takes O(1) space to store. This gives us a total of O(M ⋅ N).

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            # Option 1: We don't include text1[p1] in the solution.
            option_1 = memo_solve(p1 + 1, p2)
            
            # Option 2: We include text1[p1] in the solution, as long as
            # a match for it in text2 at or after p2 exists.
            first_occurence = text2.find(text1[p1], p2)
            option_2 = 0
            if first_occurence != -1:
                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)
            
            # Return the best option.
            return max(option_1, option_2)
                
        return memo_solve(0, 0)


## Approach 2: Improved Memoization
#######################################
# Time: O(M ⋅ N) - This time, solving each subproblem has a cost of O(1).
#                  Again, there are M ⋅ N subproblems, and so we get a total
#                  time complexity of O(M ⋅ N).
# Space: O(M ⋅ N) - We need to store the answer for each of the
#                   M ⋅ N subproblems.
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            # Recursive case 1.
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            
            # Recursive case 2.
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
            
        return memo_solve(0, 0)


## Approach 3: Dynamic Programming
######################################
# Time: O(M ⋅ N) - We're solving M ⋅ N subproblems. Solving each subproblem is
#                  an O(1) operation.
# Space: O(M ⋅ N) - We'e allocating a 2D array of size M ⋅ N to save the
#                   answers to subproblems.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Make a grid of 0's with len(text2) + 1 columns 
        # and len(text1) + 1 rows.
        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                # If the corresponding characters for this cell are the same...
                if text2[col] == text1[row]:
                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
                # Otherwise they must be different...
                else:
                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])
        
        # The original problem's answer is in dp_grid[0][0]. Return it.
        return dp_grid[0][0]


## Approach 4: Dynamic Programming with Space Optimization
##############################################################
# Let M be the length of the first word, and N be the length of the second word.

# Time: O(M ⋅ N) - Like before, we're solving M ⋅ N subproblems, and each is
#                  an O(1) operation to solve.
# Space: O(min(M, N)) - We've reduced the auxilary space required so that we
#                       only use two 1D arrays at a time; each the length of
#                       the shortest input word. Seeing as the 2 is a constant,
#                       we drop it, leaving us with the minimum length out of
#                       the two words.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        
        # The previous and current column starts with all 0's and like 
        # before is 1 more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one, and vice versa.
            previous, current = current, previous
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # If text1 doesn't reference the shortest string, swap them.
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        
        # The previous column starts with all 0's and like before is 1
        # more than the length of the first word.
        previous = [0] * (len(text1) + 1)
        
        # Iterate up each column, starting from the last one.
        for col in reversed(range(len(text2))):
            # Create a new array to represent the current column.
            current = [0] * (len(text1) + 1)
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            # The current column becomes the previous one.
            previous = current
        
        # The original problem's answer is in previous[0]. Return it.
        return previous[0]


