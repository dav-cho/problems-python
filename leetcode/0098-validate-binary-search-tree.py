##
#### 98. Validate Binar Search Tree (medium)
############################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## dfs valid range recursive
##############################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            
            left = validate(node.left, lower, node.val)
            right = validate(node.right, node.val, upper)
            return left and right
        
        return validate(root, float('-inf'), float('inf'))


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            
            left = validate(node.left, lower, node.val)
            right = validate(node.right, node.val, upper)
            return left and right
        
        return validate(root)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, lower, upper):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            
            left = validate(node.left, lower, node.val)
            right = validate(node.right, node.val, upper)
            return left and right
        
        return validate(root, float('-inf'), float('inf'))


## dfs valid range iterative
##############################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if not lower < node.val < upper:
                return False
            
            stack.append((node.left, lower, node.val))
            stack.append((node.right, node.val, upper))
            
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not lower < node.val < upper:
                return False
            
            if node.left:
                stack.append((node.left, lower, node.val))
            if node.right:
                stack.append((node.right, node.val, upper))
            
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            if node.val <= lower or node.val >= upper:
                return False
            
            if node.left:
                stack.append((node.left, lower, node.val))
            if node.right:
                stack.append((node.right, node.val, upper))
            
        return True


## dfs inorder recursive
##############################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs_inorder(node):
            if not node:
                return True
            if not dfs_inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            
            self.prev = node.val
            return dfs_inorder(node.right)
        
        self.prev = float('-inf')
        return dfs_inorder(root)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs_inorder(node, vals):
            if not node:
                return
            
            dfs_inorder(node.left, vals)
            vals.append(node.val)
            dfs_inorder(node.right, vals)
            
            return vals
            
        vals = dfs_inorder(root, [])
        for i in range(len(vals) - 1):
            if vals[i] >= vals[i + 1]:
                return False
            
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            
            self.prev = node.val
            return inorder(node.right)
        
        self.prev = float('-inf')
        return inorder(root)


## dfs inorder iterative
##############################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = float('-inf')
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
            
        return True


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()

