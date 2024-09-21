"""
112. Path Sum (easy)
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursive:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        target = targetSum - root.val
        if not (root.left or root.right):
            return target == 0
        left = self.hasPathSum(root.left, target)
        right = self.hasPathSum(root.right, target)
        return left or right


class Iterative:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum)]
        while stack:
            root, target = stack.pop()
            target -= root.val
            if not (root.left or root.right) and target == 0:
                return True
            if root.right:
                stack.append((root.right, target))
            if root.left:
                stack.append((root.left, target))
        return False


class Iterative2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, targetSum - root.val)]
        while stack:
            root, target = stack.pop()
            if not (root.left or root.right) and target == 0:
                return True
            if root.right:
                stack.append((root.right, target - root.right.val))
            if root.left:
                stack.append((root.left, target - root.left.val))
        return False
