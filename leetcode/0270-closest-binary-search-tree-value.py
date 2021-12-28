##
#### Closest Binary Search Tree Value (easy)
################################################

# Given the root of a binary search tree and a target value, return the value
# in the BST that is closest to the target.

# Example 1:
#           4
#       2       5
#     1   3
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Example 2:
# Input: root = [1], target = 4.428571
# Output: 1
 
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109

################################################################################

from typing import Optional


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## binary search
##############################
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        
        while root:
            res = min(res, root.val, key=lambda x: abs(target - x))
            
            if root.val < target:
                root = root.right
            else:
                root = root.left
                
        return res


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        
        while root:
            res = min(res, root.val, key=lambda x: abs(target - x))
            root = root.right if root.val < target else root.left
                
        return res


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        
        while root:
            closest = min(closest, root.val, key=lambda x: abs(target - x))
            
            if root.val < target:
                root = root.right
            else:
                root = root.left
                
        return closest


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = float('inf')
        
        while root:
            res = min(res, root.val, key=lambda x: abs(target - x))
            
            if root.val < target:
                root = root.right
            else:
                root = root.left
                
        return res


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = float('-inf')
        
        while root:
            res = min(res, root.val, key=lambda x: abs(target - x))
            
            if root.val < target:
                root = root.right
            else:
                root = root.left
                
        return res


## dfs inorder iterative
##############################
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack = []
        pred = float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key=lambda x: abs(target - x))
            
            pred = root.val
            root = root.right
            
        return pred


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack = []
        predecessor = float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            
            if predecessor <= target < root.val:
                return min(predecessor, root.val, key=lambda x: abs(target - x))
            
            predecessor = root.val
            root = root.right
            
        return predecessor


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        stack = []
        res = float('inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            res = min(res, root.val, key=lambda x: abs(target - x))
            root = root.right
            
        return res


## dfs inorder recursive
##############################
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs_inorder(node):
            if not node:
                return []
            
            left = dfs_inorder(node.left)
            right = dfs_inorder(node.right)
            
            return left + [node.val] + right
        
        return min(dfs_inorder(root), key=lambda x: abs(target - x))


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs_inorder(node):
            return dfs_inorder(node.left) + [node.val] + dfs_inorder(node.right) if node else []
        
        return min(dfs_inorder(root), key=lambda x: abs(target - x))


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        vals = []
        
        def dfs_inorder(node):
            if not node:
                return []
            
            left = dfs_inorder(node.left)
            vals.append(node.val)
            right = dfs_inorder(node.right)
            
            return vals
        
        return min(dfs_inorder(root), key=lambda x: abs(target - x))


## first attempt
##############################
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.res = (None, float('inf'))
        
        def dfs(node):
            if not node:
                return float('inf')
            
            curr_diff = abs(node.val - target)
            
            if curr_diff < self.res[1]:
                self.res = (node.val, curr_diff)
                
            dfs(node.left)
            dfs(node.right)
            
            return self.res[0]
        
        return dfs(root)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().closestValue([4,2,5,1,3], 3.714286), 4)
        self.assertEqual(Solution().closestValue([1], 4.428571), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursive Inorder + Linear search, O(N) time
###############################################################
# Time: O(N) - Because to build inorder traversal and then to perform linear
#              search takes linear time.
# Space: O(N) - To keep inorder traversal.
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key = lambda x: abs(target - x))


## Approach 2: Iterative Inorder, O(k) time
###############################################
# Time: O(k)
# - In the average case and O(H+k) in the worst case, where k is an index of
#   closest element. It's known that average case is a balanced tree, in that
#   case stack always contains a few elements, and hence one does 2k operations
#   to go to kth element in inorder traversal (k times to push into stack and
#   then k times to pop out of stack). That results in O(k) time complexity.
#   The worst case is a completely unbalanced tree, then you first push H
#   elements into stack and then pop out k elements, that results in
#   O(H+k) time complexity.

# Space: up to O(H)
# - To keep the stack in the case of non-balanced tree.

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(target - x))
                
            pred = root.val
            root = root.right

        return pred


## Approach 3: Binary Search, O(H) time
###########################################
# Time: O(H) - since here one goes from root down to a leaf.
# Space: O(1)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest


