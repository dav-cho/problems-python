##
#### Largest Rectangle in Histogram (hard)
##############################################

# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Example 2:
# Input: heights = [2,4]
# Output: 4

# Constraints:
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

################################################################################

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
            min_height = float('inf')
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
                calculate_area(heights, min_idx + 1, end)
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
            curr_width = len(heights) - stack[-1] -1
            max_area = max(max_area, curr_height * curr_width)
            
        return max_area


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.largestRectangleArea([2,1,5,6,2,3]), 10)
        self.assertEqual(solution.largestRectangleArea([2,4]), 4)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(N^3) - We have to find the minimum height bar O(n) lying between
#                every pair.
# Space: O(1) - Constant space is used.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                min_height = inf
                for k in range(i, j + 1):
                    min_height = min(min_height, heights[k])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area


## Approach 2: Better Brute Force
#####################################
# Time: O(n^2) - Every possible pair is considered.
# Space: O(1) - No extra space is used.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = inf
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area


## Approach 3: Divide and Conquer Approach
##############################################
# Time:
# - Average Case: O(n logn)
# - Worse Case: O(n^2) - If the numbers in the array are sorted, we don't gain
#                        the advantage of divide and conquer
# Space: O(n) - Recursion with worst case depth n.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calculateArea(heights: List[int], start: int, end: int) -> int:
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                calculateArea(heights, start, min_index - 1),
                calculateArea(heights, min_index + 1, end),
            )

        return calculateArea(heights, 0, len(heights) - 1)


## Approach 4: Better Divide and Conquer
############################################
# Time: O(n logn) - Segment tree takes log n for a total of n times.
# Space: O(n) - Space required for Segment Tree.


## Approach 5: Using Stack
##############################
# Time: O(n) - n numbers are pushed and popped.
# Space: O(n) - Stack is used.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area


