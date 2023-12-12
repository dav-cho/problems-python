"""
917. Reverse Only Letters (easy)
"""


# time: O(n)
# space: O(n)
class ReversePointer:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = []
        j = len(s) - 1

        for c in s:
            if c.isalpha():
                while not s[j].isalpha():
                    j -= 1
                ans.append(s[j])
                j -= 1
            else:
                ans.append(c)

        return "".join(ans)


# time: O(n)
# space: O(n)
class Stack:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []

        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)

        return "".join(ans)


# Two Pointers
class FirstAttempt:
    def reverseOnlyLetters(self, s: str) -> str:
        res = list(s)
        l, r = 0, len(res) - 1

        while l < r:
            if not res[l].isalpha():
                l += 1
            else:
                while l < r and not res[r].isalpha():
                    r -= 1

                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1

        return "".join(res)
