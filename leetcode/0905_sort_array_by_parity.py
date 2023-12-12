##
#### 905. Sort Array By Parity (easy)
#########################################


## two pointer - outside in
##################
# time: O(n)
# space: 0(1)
class Solution:
    def sort_array_by_parity(self, nums: list[int]) -> list[int]:
        evens, odds = 0, len(nums) - 1

        while evens < odds:
            if nums[evens] % 2 == 0:
                evens += 1
            if nums[evens] % 2 == 1:
                nums[evens], nums[odds] = nums[odds], nums[evens]
                odds -= 1

        return nums


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens, odds = 0, len(nums) - 1

        while evens < odds:
            if nums[evens] % 2 > nums[odds] % 2:
                nums[evens], nums[odds] = nums[odds], nums[evens]

            if nums[evens] % 2 == 0:
                evens += 1
            if nums[odds] % 2 == 1:
                odds -= 1

        return nums


## Tests
############

solution = Solution()

test1 = [3, 1, 2, 4]
result1 = solution.sort_array_by_parity(test1)
print(result1)
# [2, 4, 3, 1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

test2 = [0, 2]
result2 = solution.sort_array_by_parity(test2)
print(result2)
# [0, 2]

test3 = [1, 0]
result3 = solution.sort_array_by_parity(test3)
print(result3)
# [0, 1]

test4 = [1, 3]
result4 = solution.sort_array_by_parity(test4)
print(result4)
# [1, 3]
