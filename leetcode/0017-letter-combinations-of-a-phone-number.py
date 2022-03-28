##
#### 17. Letter Combinations of a Phone Number (medium)
###########################################################


## itertools module (*not valid for interview)
##################################################
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        adj_list = [numpad[digit] for digit in digits]

        return ["".join(x) for x in list(itertools.product(*adj_list))]


## backtracking
##############################
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return res

        def backtrack(i=0, curr=[]):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            for letter in numpad[digits[i]]:
                curr.append(letter)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack()

        return res


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []

        if not digits:
            return combinations

        def backtrack(idx, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            for letter in numpad[digits[idx]]:
                path.append(letter)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])

        return combinations


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i=0, curr=[]):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            for letter in numpad[digits[i]]:
                curr.append(letter)
                backtrack(i + 1, curr)
                curr.pop()

        res = []
        backtrack()

        return res


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def backtrack(i=0, curr=[]):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            for letter in numpad[digits[i]]:
                curr.append(letter)
                backtrack(i + 1, curr)
                curr.pop()

        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        if not digits:
            return res

        backtrack()

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )
        self.assertEqual(solution.letterCombinations(""), [])
        self.assertEqual(solution.letterCombinations("2"), ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
