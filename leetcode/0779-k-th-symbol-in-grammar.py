##
#### K-th Symbol in Grammar (medium)
########################################

# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
# Now in every subsequent row, we look at the previous row and replace each
# occurrence of 0 with 01, and each occurrence of 1 with 10.

# - For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd
#   row is 0110.

# Given two integer n and k, return the kth (1-indexed) symbol in the nth row
# of a table of n rows.

# Example 1:
# Input: n = 1, k = 1
# Output: 0
# Explanation: row 1: 0

# Example 2:
# Input: n = 2, k = 1
# Output: 0
# Explanation:
# row 1: 0
# row 2: 01

# Example 3:
# Input: n = 2, k = 2
# Output: 1
# Explanation:
# row 1: 0
# row 2: 01

# Example 4:
# Input: n = 3, k = 1
# Output: 0
# Explanation:
# row 1: 0
# row 2: 01
# row 3: 0110
 
# Constraints:
# 1 <= n <= 30
# 1 <= k <= 2n - 1

################################################################################

## 
##############################
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row = '0'
        for _ in range(1, n):
            row = ''.join('01' if x == '0' else '10' for x in row)

        return int(row[k - 1]) 


## using binary
##############################
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') & 1


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') % 2


## recursive
##############################
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0 if k == 1 else 1

        half = 2 ** (n - 1)
        if k <= half:
            return self.kthGrammar(n - 1, k)
        else:
            res = self.kthGrammar(n - 1, k - half)
            return 1 if res == 0 else 0


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.kthGrammar(1, 1), 0)
        self.assertEqual(solution.kthGrammar(2, 1), 0)
        self.assertEqual(solution.kthGrammar(2, 2), 1)
        self.assertEqual(solution.kthGrammar(3, 1), 0)


if __name__ == "__main__":
    unittest.main()


## Discuss Solutions
########################

## binary
##############################
# https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/113736/PythonJavaC%2B%2B-Easy-1-line-Solution-with-detailed-explanation
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') & 1


# https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/113699/Python-1-line
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count('1') % 2


## recursive
##############################
# https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/113710/Python-simple-solution-to-understand-with-explanations
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0 if k == 1 else 1

        half = 2 ** (n - 1)
        if k <= half:
            return self.kthGrammar(n - 1, k)
        else:
            res = self.kthGrammar(n - 1, k - half)
            return 1 if res == 0 else 0


## without n
##############################
# https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/121544/C%2B%2BJavaPython-Don't-need-N.-O(logK)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        res = 0
        while K > 1:
            K = K + 1 if K % 2 else K / 2
            res ^= 1
        return res


## 
##############################
# https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/158941/O(1)-space-O(n)-time-Python-8-lines-beats-100-with-explaination
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        isSame=1
        for i in range(N-1):
            if K%2 == 0 :
                isSame = -isSame
                K/=2
            else:
                K=(K+1)/2
        return 0 if isSame == 1  else 1 
