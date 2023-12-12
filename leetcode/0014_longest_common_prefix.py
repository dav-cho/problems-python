##
#### 14. Longest Common Prefix (easy)
#########################################


## horizontal scanning
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        res = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(res) != 0:
                res = res[:-1]

                if not res:
                    return ""

        return res


## vertical scanning
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]

        return strs[0]


## divide and conquer
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        def cp(left, right):
            min_len = len(min((left, right), key=len))

            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]

            return left[:min_len]

        def lcp(left, right):
            if left == right:
                return strs[left]

            mid = (left + right) // 2
            lcp_left = lcp(left, mid)
            lcp_right = lcp(mid + 1, right)

            return cp(lcp_left, lcp_right)

        return lcp(0, len(strs) - 1)


## binary search
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs or len(strs) == 0:
            return ""

        def is_common_prefix(length):
            for i in range(1, len(strs)):
                if not strs[i].startswith(strs[0][:length]):
                    return False

            return True

        min_len = len(min(strs, key=len))
        left = 1
        right = min_len

        while left <= right:
            mid = (left + right) // 2

            if is_common_prefix(mid):
                left = mid + 1
            else:
                right = mid - 1

        return strs[0][: (left + right) // 2]


## first attempt
##############################
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for j in range(1, len(strs)):
                if strs[j][i] != char:
                    return res

            res += char

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl"
        )
        self.assertEqual(solution.longestCommonPrefix(["dog", "racecar", "car"]), "")


if __name__ == "__main__":
    unittest.main()
