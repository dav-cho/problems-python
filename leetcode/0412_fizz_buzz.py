"""
412. Fizz Buzz (easy)
"""

import unittest
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for num in range(1, n + 1):
            s = ""
            if not num % 3:
                s += "Fizz"
            if not num % 5:
                s += "Buzz"
            if not s:
                s = str(num)
            res.append(s)
        return res


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        tbl = {3: "Fizz", 5: "Buzz"}
        res = []
        for num in range(1, n + 1):
            s = ""
            for k, v in tbl.items():
                if not num % k:
                    s += v
            res.append(s if s else str(num))
        return res


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for i, e in [
            (3, ["1", "2", "Fizz"]),
            (5, ["1", "2", "Fizz", "4", "Buzz"]),
            (
                15,
                [
                    "1",
                    "2",
                    "Fizz",
                    "4",
                    "Buzz",
                    "Fizz",
                    "7",
                    "8",
                    "Fizz",
                    "Buzz",
                    "11",
                    "Fizz",
                    "13",
                    "14",
                    "FizzBuzz",
                ],
            ),
        ]:
            self.assertEqual(Solution().fizzBuzz(i), e)


if __name__ == "__main__":
    unittest.main()
