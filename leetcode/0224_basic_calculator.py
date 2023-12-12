##
#### 224. Basic Calculator (hard)
########################################

##
##############################
class Solution:
    def calculate(self, s: str) -> int:
        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
        }


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.calculate("1 + 1"), 2),
        self.assertEqual(solution.calculate(" 2-1 + 2 "), 3),
        self.assertEqual(solution.calculate("(1+(4+5+2)-3)+(6+8)"), 2), 3


if __name__ == "__main__":
    unittest.main()
