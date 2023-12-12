##
#### 125. Valid Palindrome (easy)
########################################


## best
##############################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


## filter
##############################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(lambda x: x.isalnum(), [*s.lower()]))

        for i in range(len(s)):
            if s[i] != s[~i]:
                return False

        return True


## two pointer
##############################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


## reverse
##############################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list(filter(lambda char: char.isalnum(), s.lower()))

        return chars == chars[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        return chars == chars[::-1]


## first attempt
##############################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(solution.isPalindrome("race a car"), False)


if __name__ == "__main__":
    unittest.main()
