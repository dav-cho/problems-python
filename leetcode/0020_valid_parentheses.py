"""
20. Valid Parentheses (easy)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        chars = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in chars:
                top = stack.pop() if stack else ""
                if top != chars[char]:
                    return False
                continue
            stack.append(char)
        return not stack
