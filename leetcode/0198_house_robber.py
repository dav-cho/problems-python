##
#### House Robber (medium)
##############################

# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint
# stopping you from robbing each of them is that adjacent houses have
# security systems connected and it will automatically contact the
# police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money
# of each house, return the maximum amount of money you can rob
# tonight without alerting the police.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9)
# and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

##########################################################################

# nums --> amount of money in each house
# return --> max amount of money you can rob without alerting police


def rob(nums: list[int]) -> int:
    prev_max = 0
    curr_max = 0

    for num in nums:
        prev_max, curr_max = curr_max, max(prev_max + num, curr_max)

    return curr_max


def rob(nums: list[int]) -> int:
    dp = []
    N = len(nums)

    if N is 0:
        return 0
    if N is 1:
        return nums[0]

    dp.extend([nums[0], max(nums[0], nums[1])])

    for i in range(2, N):
        dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))

    return dp[N - 1]


# Approach 1: Recursion with Memoization
# time: O(N) - at most process N recursive calls thanks to caching
# space: O(N) - occupied by cache and recursion stack
def rob(nums: list[int]) -> int:
    robbed = {}

    def rob_from(index, nums):
        # no more houses left to examine
        if index >= len(nums):
            return 0

        # return caches value
        if index in robbed:
            return robbed[index]

        ans = max(rob_from(index + 1, nums), rob_from(index + 1, nums) + nums[index])

        # cache for future use
        robbed[index] = ans

        return ans

    return rob_from(0, nums)


# Approach 2: Dynamic Programming
# time: O(N) - we loop from N - 2...0 but we use pre-calculated values
#               from the table which is constant time
# space: O(N) - used by the table
#              - the advantage here is that we don't have a recursion stack,
#                so when the number of houses is large, we won't run
#                into stack overflow problems
def rob(nums: list[int]) -> int:
    # special handling for empty cases
    if not nums:
        return 0

    max_robbed_amount = [None for _ in range(len(nums) + 1)]
    N = len(nums)

    # base case initialization
    max_robbed_amount[N], max_robbed_amount[N - 1] = 0, nums[N - 1]

    # Dynamic programming table calculations
    for i in range(N - 2, -1, -1):
        max_robbed_amount[i] = max(
            max_robbed_amount[i + 1], max_robbed_amount[i + 2] + nums[i]
        )

    return max_robbed_amount[0]


# Approach 3: Optimized Dynamic Programming
# time:
# space:
def rob(nums: list[int]) -> int:
    if not nums:
        return 0

    N = len(nums)
    rob_next_next = 0
    rob_next = nums[N - 1]

    for i in range(N - 2, -1, -1):
        current = max(rob_next, rob_next_next + nums[i])
        rob_next_next = rob_next
        rob_next = current

    return rob_next


robResult1 = rob([1, 2, 3, 1])  # 4
robResult2 = rob([2, 7, 9, 3, 1])  # 12
print(robResult1)
print(robResult2)
