##
#### 1051. Height Checker (easy)
####################################


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

test1 = [1, 1, 4, 2, 1, 3]
# 3, [1,1,1,2,3,4]
test2 = [5, 1, 2, 3, 4]
# 5, [1,2,3,4,5]
test3 = [1, 2, 3, 4, 5]
# 0, [1,2,3,4,5]

solution = Solution()
print(solution.height_checker(test1))
print(solution.height_checker(test2))
print(solution.height_checker(test3))
