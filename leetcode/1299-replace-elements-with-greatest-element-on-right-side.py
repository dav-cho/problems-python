##
#### Replace Elements with Greatest Element on Right Side (easy)
####################################################################

# Given an array arr, replace every element in that array with the
# greatest element among the elements to its right, and replace the
# last element with -1.

# After doing so, return the array.

# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation:
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# Example 2:
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

# Constraints:
# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105

###################################################################################


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        for i in range(len(arr) - 1):
            max = i + 1

            for j in range(i + 1, len(arr)):
                if arr[j] > arr[max]:
                    max = j

            arr[i] = arr[max]

        arr[-1] = -1

        return arr


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        mx = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])

        return arr


## Tests
############

test1 = [17, 18, 5, 4, 6, 1]  # [18, 6, 6, 6, 1, -1]
test2 = [400]  # [-1]
test3 = [57010, 40840, 69871, 14425, 70605]  # [70605, 70605, 70605, 70605, -1]


def test(*args):
    solution = Solution()
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            print(test)

            result = solution.replaceElements(test)
            count += 1

            print(result)

    return run()


test(test1, test2, test3)

## LeetCode Solutions
#########################
## (None)
