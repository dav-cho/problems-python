"""
101. Symmetric Tree (easy)
"""

from collections import deque
from typing import Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursive:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Don't need necessarily need this, but type checker complains without
        # on last line: return is_mirror(root.left, root.right)
        #   "left" is not a known member of "None"
        #   "right" is not a known member of "None"
        if not root:
            return False

        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            outside = is_mirror(left.left, right.right)
            inside = is_mirror(left.right, right.left)
            return outside and inside

        return is_mirror(root.left, root.right)


class Iterative:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue: List[Optional[TreeNode]] = [root, root]
        while queue:
            left, right, *queue = queue
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            queue.extend([left.left, right.right, left.right, right.left])
        return True


class Iterative2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue = [root, root]
        while queue:
            left, right, *queue = queue
            if not (left or right):
                continue
            if not (left and right) or left.val != right.val:
                return False
            queue.extend([left.left, right.right, left.right, right.left])
        return True


class IterativeDeque:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue: Deque[Optional[TreeNode]] = deque([root, root])
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            queue.extend([left.left, right.right, left.right, right.left])
        return True


class RecursiveXOR:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not (left or right):
                return True
            if bool(left) ^ bool(right):
                return False
            if left.val != right.val:
                return False
            outside = is_mirror(left.left, right.right)
            inside = is_mirror(left.right, right.left)
            return outside and inside

        return is_mirror(root.left, root.right)


class IterativeXOR:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        queue: List[Optional[TreeNode]] = [root, root]
        while queue:
            left, right, *queue = queue
            if not (left or right):
                continue
            if bool(left) ^ bool(right):
                return False
            if left.val != right.val:
                return False
            queue.extend([left.left, right.right, left.right, right.left])
        return True
