##
#### Single Number (easy)
#############################

# Given a non-empty array of integers nums, every element
# appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity
# and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one
# element which appears only once.

#############################################################################


from collections import Counter


def singleNumber(nums: list[int]) -> int:
    counts = Counter(nums)

    if len(nums) < 2:
        return nums[0]

    for num in counts:
        if counts[num] == 1:
            return num


# Approach 3: Math
# 2 * (a + b + c) - (a + a + b + b + c) = c
def singleNumber(nums: list[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)


test1 = [2, 2, 1]  # 1
test2 = [4, 1, 2, 1, 2]  # 4
test3 = [1]  # 1


def test(*args):
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = singleNumber(test)
            print(f"test: {count}")
            print(f"result {count}: {result}")

    return run()


test(test1, test2, test3)
