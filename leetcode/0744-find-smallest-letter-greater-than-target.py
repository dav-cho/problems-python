##
#### 744. Find Smallest Letter Greater Than Target (easy)
#############################################################


from bisect import bisect


## binary search
##############################
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        idx = bisect(letters, target)

        return letters[idx % len(letters)]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        idx = bisect.bisect(letters, target)

        return letters[idx] if idx < len(letters) else letters[0]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        res = 0

        while left <= right:
            mid = (left + right) >> 1

            if letters[mid] > target:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return letters[res]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        res = 0

        while left <= right:
            mid = (left + right) >> 1

            if letters[mid] <= target:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return letters[res]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]

        left, right = 0, len(letters) - 1

        while left < right:
            mid = (left + right) >> 1

            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1

        return letters[left]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]

        left, right = 0, len(letters) - 1

        while left < right:
            mid = (left + right) >> 1

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) >> 1

            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return letters[left % len(letters)]


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        if letters[left] > target or letters[right] < target:
            return letters[left]

        while left <= right:
            mid = (left + right) >> 1

            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return letters[left % len(letters)]


## linear scan
##############################
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for char in letters:
            if char > target:
                return char

        return letters[0]


## hash table
##############################
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        seen = set(letters)

        for i in range(1, 26):
            char = chr((ord(target) - ord("a") + i) % 26 + ord("a"))

            if char in seen:
                return char


##
##############################
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().nextGreatestLetter(["c", "f", "j"], "a"), "c")
        self.assertEqual(Solution().nextGreatestLetter(["c", "f", "j"], "c"), "f")
        self.assertEqual(Solution().nextGreatestLetter(["c", "f", "j"], "d"), "f")


if __name__ == "__main__":
    unittest.main()
