"""
977. Squares of a Sorted Array (easy)
"""


# O(n) solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = [0] * (r + 1)

        for i in range(r, -1, -1):
            if abs(nums[l]) < nums[r]:
                num = nums[r]
                r -= 1
            else:
                num = nums[l]
                l += 1
            ans[i] = num * num

        return ans


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length
        l = 0
        r = length - 1

        for i in range(length):
            if abs(nums[l]) < abs(nums[r]):
                num = nums[r]
                r -= 1
            else:
                num = nums[l]
                l += 1
            ans[~i] = num * num

        return ans


# brute force
class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        return sorted(num**2 for num in nums)


## Tests
############

test1 = [-4, -1, 0, 3, 10]  # [0, 1, 9, 16, 100]
test2 = [-7, -3, 2, 3, 11]  # [4, 9, 9, 49, 121]

solution = Solution()
print(solution.sorted_squares(test1))
print(solution.sorted_squares(test2))
