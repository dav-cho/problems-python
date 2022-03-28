##
#### 20. Valid Parentheses (easy)
#####################################


## stack
##############################
class Solution:
    def isValid(self, s: str) -> bool:
        table = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in table:
                if stack and stack[-1] == table[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack


## first attempt
##############################
class Solution:
    def isValid(self, s: str) -> bool:
        table = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in table:
                if stack and stack[-1] == table[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().isValid("()"), True)
        self.assertEqual(Solution().isValid("()[]{}"), True)
        self.assertEqual(Solution().isValid("(]"), False)
        self.assertEqual(Solution().isValid("([)]"), False)
        self.assertEqual(Solution().isValid("{[]}"), True)


if __name__ == "__main__":
    unittest.main()
