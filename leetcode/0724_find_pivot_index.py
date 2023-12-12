##
#### 724. Find Pivot Index (easy)
#####################################


## prefix sum
#####################
class Solution:
    def pivot_index(self, nums: list[int]) -> int:
        left, right = 0, sum(nums)
        for i, num in enumerate(nums):
            if left == right - left - num:
                return i
            left += num

        return -1


## sliding window
#####################
class Solution:
    def pivot_index(self, nums: list[int]) -> int:
        left, right = 0, sum(nums)

        for i in range(len(nums)):
            right -= nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1


## brute force
##################
class Solution:
    def pivot_index(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1 :]):
                return i

        return -1


## Tests
############

test1 = [1, 7, 3, 6, 5, 6]  # 3
test2 = [1, 2, 3]  # -1
test3 = [2, 1, -1]  # 0

solution = Solution()
print(solution.pivot_index(test1))
print(solution.pivot_index(test2))
print(solution.pivot_index(test3))
