##
#### Convert Sorted Array to Binary Search Tree (easy)
##########################################################

# Given an integer array nums where the elements are sorted in
# ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth
# of the two subtrees of every node never differs by more than one.

# Example 1:
#             0                   0
#        -3       9   -->   -10      5
#   -10        5               -3      9
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
#     3  -->  1
#   1           3
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

##############################################################################
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


## Approach 1: Preorder Traversal - Always Choose Left Middle Node as a Root
################################################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        pass


## Approach 2: Preorder Traversal - Always Choose Right Middle Node as a Root
#################################################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        pass


## Approach 3: Preorder Traversal - Choose Random Middle Node as a Root
###########################################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        pass


def sortedArrayToBST(nums: list[int]) -> TreeNode:
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid + 1 :]

    root = TreeNode(nums[mid])
    root.left = TreeNode(left[0])
    root.right = TreeNode(right[-1])

    current = root.left
    for i in range(1, len(left)):
        if not current.left:
            current.left = TreeNode(left[i])
        elif not current.right:
            current.right = TreeNode(left[i])

    current = root.right
    for i in range(len(right), -1, -1):
        if not current.left:
            current.left = TreeNode(right[i])
        elif not current.right:
            current.right = TreeNode(right[i])


test1 = [-10, -3, 0, 5, 9]  # [0,-3,9,-10,null,5]
test2 = [1, 3]  # [3, 1]


def test(*args):
    count = 1

    def run():
        for test in args:
            result = sortedArrayToBST(test)
            nonlocal count
            print(f"~ test {count}")
            print(f"{test} --> {result}")

    return run()


test(test1, test2)


## LeetCode Solutions
#########################

## Approach 1: Preorder Traversal - Always Choose Left Middle Node as a Root
################################################################################
# time: O(n) - visit each node exactly once
# space: O(n) - to keep the output and O(log(n)) for the recursion stack
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)


## Approach 2: Preorder Traversal - Always Choose Right Middle Node as a Root
#################################################################################
# time: O(n) - same as Approach 1
# space: O(n) - same as Approach 1
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # always choose right middle node as a root
            p = (left + right) // 2
            if (left + right) % 2:
                p += 1

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)


## Approach 3: Preorder Traversal - Choose Random Middle Node as a Root
###########################################################################
# time: O(n) - same as Approach 1
# space: O(n) - same as Approach 1
from random import randint


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # choose random middle node as a root
            p = (left + right) // 2
            if (left + right) % 2:
                p += randint(0, 1)

            # preorder traversal: node -> left -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)
