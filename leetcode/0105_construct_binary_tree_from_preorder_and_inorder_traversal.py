##
#### 105. Construct Binary Tree from Preorder and Inorder Traversal (medium)
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

