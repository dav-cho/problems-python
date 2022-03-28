##
#### 106. Construct Binary Tree from Inorder and Postorder Traversal (medium)
#################################################################################


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

