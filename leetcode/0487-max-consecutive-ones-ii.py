##
#### 487. Max Consecutive Ones II (medium)
##############################################


## sliding window - two pointers
class Solution:
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        left = right = mx = zeroes = 0

        while right < len(nums):
            if nums[right] == 0:
                zeroes += 1

            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1

                left += 1

            mx = max(mx, right - left + 1)
            right += 1

        return mx


## Tests
############

test1 = [1, 0, 1, 1, 0]  # 4
test2 = [1, 0, 1, 1, 0, 1]  # 4
test3 = [1, 1, 0, 1]  # 4

solution = Solution()
print(solution.find_max_consecutive_ones(test1))
print(solution.find_max_consecutive_ones(test2))
print(solution.find_max_consecutive_ones(test3))
