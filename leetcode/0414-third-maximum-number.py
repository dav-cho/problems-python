##
#### Third Maximum Number (easy)
####################################

# Given integer array nums, return the third maximum number in this array.
# If the third maximum does not exist, return the maximum number.
 
# Example 1:
# Input: nums = [3,2,1]
# Output: 1
# Explanation: The third maximum is 1.

# Example 2:
# Input: nums = [1,2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is
# returned instead.

# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.

# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

################################################################################


## brute force - sorting
class Solution:
    def third_max(self, nums: list[int]) -> int:
        nums = sorted(set(nums), reverse = True)
        
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

test1 = [3, 2, 1]       # 1
test2 = [1, 2]          # 2
test3 = [2, 2, 3, 1]    # 1
test4 = [12, 3, 8, 9, 12, 12, 7, 8, 12, 4, 3, 8, 1]     # 8

solution = Solution()
print(solution.third_max(test1))
print(solution.third_max(test2))
print(solution.third_max(test3))
print(solution.third_max(test4))


## LeetCode Solutions
#########################

## Approach 1: Use a Set and Delete Maximums
################################################
# time: O(n) - creating a HashSet costs O(n), since we have to place n values,
#              and placing each one costs O(1).
#              Finding the max 3 times costs O(3n) --> O(n)
# space: O(n) - we use a hashset which requires at most O(n) extra space
class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        # Make a Set with the input.
        nums = set(nums)

        # Find the maximum.
        maximum = max(nums)

        # Check whether or not this is a case where
        # we need to return the *maximum*.
        if len(nums) < 3:
            return maximum

        # Otherwise, continue on to finding the third maximum.
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)


## Approach 2: Seen-Maximums Set
####################################
# time: O(n) - need to find the at most 3 maxes, which is O(3n)
# space: O(1) - seen maximums set of length 3 is negligible
#               - no extra space used
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        
        def maximum_ignoring_seen_maximums(nums, seen_maximums):
            maximum = None
            for num in nums:
                if num in seen_maximums:
                    continue
                if maximum == None or num > maximum:
                    maximum = num
            return maximum

        seen_maximums = set()

        for _ in range(3):
            current_maximum = maximum_ignoring_seen_maximums(nums, seen_maximums)
            if current_maximum == None:
                return max(seen_maximums)
            seen_maximums.add(current_maximum)

        return min(seen_maximums)


## Approach 3: Keep Track of 3 Maximums Using a Set
#######################################################
# time: O(n) - insertion into set costs O(1), but we must loop atleast once
# space: O(1) - HashSet of length 3 is negligible. No extra space needed.
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        maximums = set()
        for num in nums:
            maximums.add(num)
            if len(maximums) > 3:
                maximums.remove(min(maximums))
        if len(maximums) == 3:
            return min(maximums)
        return max(maximums)

