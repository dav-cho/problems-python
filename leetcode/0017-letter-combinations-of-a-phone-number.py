##
#### Letter Combinations of a Phone Number (medium)
#######################################################

# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.

# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

################################################################################

## itertools module (*not valid for interview)
##################################################
import itertools

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        numpad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        adj_list = [numpad[digit] for digit in digits]
        
        return [''.join(x) for x in list(itertools.product(*adj_list))]


## backtracking
##############################
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        numpad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        if not digits:
            return res
        
        def backtrack(i=0, curr=[]):
            if len(curr) == len(digits):
                res.append(''.join(curr))
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
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        combinations = []
        
        if not digits:
            return combinations
        
        def backtrack(idx, path):
            if len(path) == len(digits):
                combinations.append(''.join(path))
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
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        def backtrack(i=0, curr=[]):
            if len(curr) == len(digits):
                res.append(''.join(curr))
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
                res.append(''.join(curr))
                return
            
            for letter in numpad[digits[i]]:
                curr.append(letter)
                backtrack(i + 1, curr)
                curr.pop()

        numpad = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
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
        self.assertEqual(solution.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
        self.assertEqual(solution.letterCombinations(""), [])
        self.assertEqual(solution.letterCombinations("2"), ["a","b","c"])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Backtracking
##############################
# Time: O(4^N ⋅N) - Where N is the length of digits. Note that 4 in this
#                   expression is referring to the maximum value length in the
#                   hash map, and not to the length of the input.
# - The worst-case is where the input consists of only 7s and 9s. In that case,
#   we have to explore 4 additional paths for every extra digit. Then, for each
#   combination, it costs up to N to build the combination. This problem can be
#   generalized to a scenario where numbers correspond with up to M digits, in
#   which case the time complexity would be O(M^N ⋅N). For the problem
#   constraints, we're given, M=4, because of digits 7 and 9 having 4 letters
#   each.

# Space: O(N) - where N is the length of digits.
# - Not counting space used for the output, the extra space we use relative to
#   input size is the space occupied by the recursion call stack. It will only
#   go as deep as the number of digits in the input since whenever we reach that
#   depth, we backtrack.
# - As the hash map does not grow as the inputs grows, it occupies O(1) space.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0: 
            return []
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            
            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations


