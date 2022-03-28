##
#### 84. Largest Rectangle in Histogram (hard)
##############################################


## best - using stack
##############################
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = [-1]
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area


## brute force (TLE)
##############################
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            min_height = float("inf")
            for j in range(i, n):
                min_height = min(min_height, heights[j])
                width = j - i + 1
                max_area = max(max_area, min_height * width)

        return max_area


## divide and conquer (TLE)
##############################
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        def calculate_area(heights, start, end):
            if start > end:
                return 0

            min_idx = start
            for i in range(start, end + 1):
                if heights[min_idx] > heights[i]:
                    min_idx = i

            return max(
                heights[min_idx] * (end - start + 1),
                calculate_area(heights, start, min_idx - 1),
                calculate_area(heights, min_idx + 1, end),
            )

        return calculate_area(heights, 0, len(heights) - 1)


## using stack
##############################
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                max_area = max(max_area, curr_height * curr_width)
            stack.append(i)

        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, curr_height * curr_width)

        return max_area


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(solution.largestRectangleArea([2, 4]), 4)


if __name__ == "__main__":
    unittest.main()
