##
#### Construct Binary Tree from Inorder and Postorder Traversal (medium)
############################################################################

# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.

# Example 1:
#       3
#    9     20
#        15  7
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 
# Constraints:
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

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
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def dfs_postorder(left, right):
            if left > right:
                return
            
            root = TreeNode(postorder.pop())
            idx = idx_map[root.val]
            root.right = dfs_postorder(idx + 1, right)
            root.left = dfs_postorder(left, idx - 1)
            
            return root
        
        return dfs_postorder(0, len(inorder) - 1)


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(left, right):
            if left > right:
                return
            
            root = TreeNode(postorder.pop())
            i = idx_map[root.val]
            
            root.right = helper(i + 1, right)
            root.left = helper(left, i - 1)
            return root
        
        return helper(0, len(inorder) - 1)


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(inorder_left_bound, inorder_right_bound):
            if inorder_left_bound > inorder_right_bound:
                return
            
            root = TreeNode(postorder.pop())
            idx = idx_map[root.val]
            
            root.right = helper(idx + 1, inorder_right_bound)
            root.left = helper(inorder_left_bound, idx - 1)
            return root
        
        return helper(0, len(inorder) - 1)


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return
            
            root = TreeNode(postorder.pop())
            idx = idx_map[root.val]
            
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            return root
        
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return
            
            val = postorder.pop()
            root = TreeNode(val)
            idx = idx_map[val]
            
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            
            return root
        
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)



## 
##############################
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
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

## Approach 1: Recursion
##############################
# Time: O(N)
# - Let's compute the solution with the help of master theorem
#   T(N) = aT(b/N) + Θ(N^d). The equation represents dividing the problem up
#   into a subproblems of size (N/b) in Θ(N^d) time. Here one divides the
#   problem in two subproblemes a = 2, the size of each subproblem (to compute
#   left and right subtree) is a half of initial problem b = 2, and all this
#   happens in a constant time d = 0. That means that log_b(a) > d and hence
#   we're dealing with case 1 that means O(N^(log_b(a))) = O(N) time complexity.
# Space: O(N) - Since we store the entire tree.
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]
 
            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root
        
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)


