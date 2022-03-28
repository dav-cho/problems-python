##
#### 779. K-th Symbol in Grammar (medium)
#############################################


##
##############################
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row = "0"
        for _ in range(1, n):
            row = "".join("01" if x == "0" else "10" for x in row)

        return int(row[k - 1])


## using binary
##############################
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count("1") & 1


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k - 1).count("1") % 2


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
