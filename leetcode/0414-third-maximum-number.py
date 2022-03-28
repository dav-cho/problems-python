##
#### 414. Third Maximum Number (easy)
#########################################


## brute force - sorting
class Solution:
    def third_max(self, nums: list[int]) -> int:
        nums = sorted(set(nums), reverse=True)

        return nums[2] if len(nums) > 2 else nums[0]


## one pass
class Solution:
    def third_max(self, nums: list[int]) -> int:
        pass


## approach 1
class Solution:
    def third_max(self, nums: list[int]) -> int:
        nums = set(nums)

        if len(nums) < 3:
            return max(nums)

        nums.remove(max(nums))
        nums.remove(max(nums))

        return max(nums)


## approach 2
class Solution:
    def third_max(self, nums: list[int]) -> int:
        seen = set()

        for _ in range(3):
            mx = float("-inf")

            for num in nums:
                if num > mx and num not in seen:
                    mx = num

            if mx != float("-inf"):
                seen.add(mx)

        if len(seen) <= 2:
            return max(seen)

        return min(seen)


## apporach 3
class Solution:
    def third_max(self, nums: list[int]) -> int:
        maxes = set()

        for num in nums:
            maxes.add(num)

            while len(maxes) > 3:
                maxes.remove(min(maxes))

        if len(maxes) < 3:
            return max(maxes)

        return min(maxes)


## Tests
############

test1 = [3, 2, 1]  # 1
test2 = [1, 2]  # 2
test3 = [2, 2, 3, 1]  # 1
test4 = [12, 3, 8, 9, 12, 12, 7, 8, 12, 4, 3, 8, 1]  # 8

solution = Solution()
print(solution.third_max(test1))
print(solution.third_max(test2))
print(solution.third_max(test3))
print(solution.third_max(test4))
