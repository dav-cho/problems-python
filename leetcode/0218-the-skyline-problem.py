##
#### The Skyline Problem (hard)
###################################

# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Given the locations and
# heights of all the buildings, return the skyline formed by these buildings
# collectively.

# The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

# lefti is the x coordinate of the left edge of the ith building.
# righti is the x coordinate of the right edge of the ith building.
# heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.

# The skyline should be represented as a list of "key points" sorted by their
# x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left
# endpoint of some horizontal segment in the skyline except the last point in
# the list, which always has a y-coordinate 0 and is used to mark the skyline's
# termination where the rightmost building ends. Any ground between the leftmost
# and rightmost buildings should be part of the skyline's contour.

# Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

# Example 1:
# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.

# Example 2:
# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
 
# Constraints:
# 1 <= buildings.length <= 104
# 0 <= lefti < righti <= 231 - 1
# 1 <= heighti <= 231 - 1
# buildings is sorted by lefti in non-decreasing order.

################################################################################

## divide and conquer
##############################
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]
        
        left = self.getSkyline(buildings[:n // 2])
        right = self.getSkyline(buildings[n // 2:])
        
        return self.merge_skylines(left, right)
    
    def merge_skylines(self, left, right):
        def update_output(x, y):
            if not res or res[-1][0] != x:
                res.append([x, y])
            else:
                res[-1][1] = y
                
        def append_skyline(p, lst, n, y, curr_y):
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y
                
        n_left, n_right = len(left), len(right)
        p_left = p_right = 0
        curr_y = left_y = right_y = 0
        res = []
        
        while p_left < n_left and p_right < n_right:
            point_left, point_right = left[p_left], right[p_right]
            if point_left[0] < point_right[0]:
                x, left_y = point_left
                p_left += 1
            else:
                x, right_y = point_right
                p_right += 1
                
            max_y = max(left_y, right_y)
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y
                
        append_skyline(p_left, left, n_left, left_y, curr_y)
        append_skyline(p_right, right, n_right, right_y, curr_y)
        
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]), [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])
        self.assertEqual(solution.getSkyline([[0,2,3],[2,5,3]]), [[0,3],[5,0]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Divide and Conquer
#####################################
# Time: O(N logN) - Where N is the number of buildings. The problem is an
#                   example of Master Theorem case II: T(N) = 2T(N/2) + 2N, that
#                   results in O(N logN) time complexity.
# Space: O(N) - We use the output variable to keep track of the results.
class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        """
        Divide-and-conquer algorithm to solve skyline problem,
        which is similar with the merge sort algorithm.
        """
        n = len(buildings)
        # The base cases
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        # If there is more than one building,
        # recursively divide the input into two subproblems.
        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2 :])

        # Merge the results of subproblem together.
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):
        """
        Merge two skylines together.
        """
        def update_output(x, y):
            """
            Update the final output with the new element.
            """
            # if skyline change is not vertical -
            # add the new point
            if not output or output[-1][0] != x:
                output.append([x, y])
            # if skyline change is vertical -
            # update the last point
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, y, curr_y):
            """
            Append the rest of the skyline elements with indice (p, n)
            to the final output.
            """
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_l, n_r = len(left), len(right)
        p_l = p_r = 0
        curr_y  = left_y = right_y = 0
        output = []

        # while we're in the region where both skylines are present
        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            # pick up the smallest x
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1
            # max height (i.e. y) between both skylines
            max_y = max(left_y, right_y)
            # if there is a skyline change
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        # there is only left skyline
        append_skyline(p_l, left, n_l, left_y, curr_y)

        # there is only right skyline
        append_skyline(p_r, right, n_r, right_y, curr_y)

        return output


