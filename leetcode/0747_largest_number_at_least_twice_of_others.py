##
#### 747. Largest Number At Least Twice of Others (easy)
############################################################


## two pass
###############
class Solution:
    def dominant_index(self, nums: list[int]) -> int:
        mx = max(nums)

        for i in range(len(nums)):
            if nums[i] == mx:
                idx = i
            else:
                if mx < nums[i] * 2:
                    return -1

        return idx


## Tests
############

test1 = [3, 6, 1, 0]  # 1
test2 = [1, 2, 3, 4]  # -1
test3 = [1]  # 0

solution = Solution()
print(solution.dominant_index(test1))
print(solution.dominant_index(test2))
print(solution.dominant_index(test3))
