##
#### Construct Binary Tree from Preorder and Inorder Traversal (medium)
###########################################################################

# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.

# Example 1:
#       3
#    9     20
#        15  7
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 
# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

################################################################################

from typing import Optional


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
##############################
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        inorder_idx_map = {val: i for i, val in enumerate(inorder)}
        self.preorder_idx = 0
        
        def helper(left, right):
            if left > right:
                return
            
            root = TreeNode(preorder[self.preorder_idx])
            self.preorder_idx += 1
            i = inorder_idx_map[root.val]
            
            root.left = helper(left, i - 1)
            root.right = helper(i + 1, right)
            return root
        
        return helper(0, len(inorder) - 1)


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        inorder_idx_map = {val: i for i, val in enumerate(inorder)}
        preorder_idx = 0
        
        def helper(left, right):
            nonlocal preorder_idx
            
            if left > right:
                return
            
            root = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            i = inorder_idx_map[root.val]
            
            root.left = helper(left, i - 1)
            root.right = helper(i + 1, right)
            return root
        
        return helper(0, len(preorder) - 1)


## first attempt
##############################
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(left, right):
            if left > right:
                return
            
            root = ListNode(preorder.pop(0))
            i = idx_map[root.val]
            
            root.left = helper(left, i - 1)
            root.right = helper(i + 1, right)
            return root
        
        return helper(0, len(inorder) - 1)


## 
##############################
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )
        self.assertCountEqual()


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: 
##############################
# Time: 
# Space: 


## Approach 2: 
##############################
# Time: 
# Space: 


## Approach 3: 
##############################
# Time: 
# Space: 


