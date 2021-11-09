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

################################################################################

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
## dfs preorder - choose left as root - recursive
#####################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)


## dfs preorder - choose left as root - iterative
#####################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        root = TreeNode(nums[right // 2])
        stack = [(root, left, right)]
        
        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2
            
            if left < mid:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left, mid - 1))
            if right > mid:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid + 1, right))
                
        return root


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        root = TreeNode(nums[right // 2])
        stack = [(root, left, right)]
        
        while stack:
            node, left, right = stack.pop()
            if not node:
                continue
                
            mid = (left + right) // 2
            if left < mid:
                node.left = TreeNode(nums[(left + mid - 1) // 2])
                stack.append((node.left, left, mid - 1))
            if right > mid:
                node.right = TreeNode(nums[(mid + 1 + right) // 2])
                stack.append((node.right, mid + 1, right))
                
        return root


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        root = TreeNode(nums[right // 2])
        stack = [(root, left, right)]
        
        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2
            
            if left > right:
                continue
            
            if left < mid:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left, mid - 1))
            if right > mid:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid + 1, right))
                
        return root


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        root = TreeNode(nums[right // 2])
        queue = deque([(root, left, right)])
        
        while queue:
            node, left, right = queue.popleft()
            
            if left > right:
                continue

            mid = (left + right) // 2
            
            if left < mid:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                queue.append((node.left, left, mid - 1))
            if right > mid:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                queue.append((node.right, mid + 1, right))
                
        return root


## dfs preorder - choose right as root - recursive
######################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            
            if (left + right) % 2:
                mid += 1
            
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)


## dfs preorder - choose right as root - iterative
######################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        pass


## dfs preorder - choose random middle node as root - recursive
###################################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            
            if (left + right) % 2:
                mid += randint(0, 1)
            
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
        
        return helper(0, len(nums) - 1)


## dfs preorder - choose random middle node as root - iterative
###################################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Preorder Traversal: Always Choose Left Middle Node as a Root
###############################################################################
# Time: O(N) - Since we visit each node exactly once.
# Space: O(logN) - The recursion stack requires O(logN) space because the tree
#                  is height-balanced. Note that the O(N) space used to store
#                  the output does not count as auxiliary space, so it is not
#                  included in the space complexity.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
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


## Approach 2: Preorder Traversal: Always Choose Right Middle Node as a Root
###############################################################################
# Time: O(N)- Since we visit each node exactly once.
# Space: O(logN) - The recursion stack requires O(logN) space because the tree
#                  is height-balanced. Note that the O(N) space used to store
#                  the output does not count as auxiliary space, so it is not
#                  included in the space complexity.
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:        
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


## Approach 3: Preorder Traversal: Choose Random Middle Node as a Root
##########################################################################
# Time: O(N) - Since we visit each node exactly once.
# Space: O(logN) - The recursion stack requires O(logN) space because the tree
#                  is height-balanced. Note that the O(N) space used to store
#                  the output does not count as auxiliary space, so it is not
#                  included in the space complexity.

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


