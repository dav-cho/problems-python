##
#### Height Checker (easy)
##############################

# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing
# order by height. Let this ordering be represented by the integer array
# expected where expected[i] is the expected height of the ith student in line.
 
# You are given an integer array heights representing the current order that
# the students are standing in. Each heights[i] is the height of the
# ith student in line (0-indexed).
 
# Return the number of indices where heights[i] != expected[i].
 
# Example 1:
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

# Example 2:
# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]
# All indices do not match.

# Example 3:
# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.
  
 
# Constraints:
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100

################################################################################


class Solution:
    def height_checker(self, heights: list[int]) -> int:
        copy = sorted(heights)
        count = 0

        for i, num in enumerate(heights):
            if num != copy[i]:
                count += 1

        return count


class Solution:
    def height_checker(self, heights: list[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


## Tests
############

test1 = [1,1,4,2,1,3]
# 3, [1,1,1,2,3,4]
test2 = [5,1,2,3,4]
# 5, [1,2,3,4,5]
test3 = [1,2,3,4,5]
# 0, [1,2,3,4,5]

solution = Solution()
print(solution.height_checker(test1))
print(solution.height_checker(test2))
print(solution.height_checker(test3))

