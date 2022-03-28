##
#### 977. Squares of a Sorted Array (easy)
##############################################


## brute force
##################
class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        return sorted(num**2 for num in nums)


## O(n) solution
####################
class Solution:
    def sorted_squares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [None] * n
        left, right = 0, n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1

            result[i] = square**2

        return result


## Tests
############

test1 = [-4, -1, 0, 3, 10]  # [0, 1, 9, 16, 100]
test2 = [-7, -3, 2, 3, 11]  # [4, 9, 9, 49, 121]

solution = Solution()
print(solution.sorted_squares(test1))
print(solution.sorted_squares(test2))
