##
#### 163. Missing Ranges (easy)
########################################


## linear scan
##############################
class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        res = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 < curr - 1:
                res.append(f"{prev + 1}->{curr - 1}")
            elif prev + 1 == curr - 1:
                res.append(str(prev + 1))
            prev = curr

        return res


class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        def format_range(lower, upper):
            if lower == upper:
                return str(lower)
            return f"{lower}->{upper}"

        res = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                res.append(format_range(prev + 1, curr - 1))
            prev = curr

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99),
            ["2", "4->49", "51->74", "76->99"],
        )
        self.assertEqual(Solution().findMissingRanges([], 1, 1), ["1"])
        self.assertEqual(Solution().findMissingRanges([], -3, -1), ["-3->-1"])
        self.assertEqual(Solution().findMissingRanges([-1], -1, -1), [])
        self.assertEqual(Solution().findMissingRanges([-1], -2, -1), ["-2"])


if __name__ == "__main__":
    unittest.main()
