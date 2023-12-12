##
#### 448. Find All Numbers Disappeared in an Array (easy)
#############################################################


## subtract 2 sets
######################
class Solution:
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


## use hash map
###################
class Solution:
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        length, nums = len(nums) + 1, set(nums)

        return [x for x in range(1, length) if x not in nums]


## in place markers
#######################
class Solution:
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1

            if nums[idx] > 0:
                nums[idx] *= -1

        result = []
        for j in range(1, len(nums) + 1):
            if nums[j - 1] > 0:
                result.append(j)

        return result

        # return [j for j in range(1, len(nums) + 1) if nums[j - 1] > 0]


## Tests
############

test1 = [4, 3, 2, 7, 8, 2, 3, 1]  #  [5,6]
test2 = [1, 1]  # [2]

solution = Solution()
print(solution.find_disappeared_numbers(test1))
print(solution.find_disappeared_numbers(test2))
