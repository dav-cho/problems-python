"""
102. Binary Tree Level Order Traversal (medium)
"""

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursive:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(node: Optional[TreeNode], level: int) -> List[List[int]]:
            if not node:
                return res
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
            return res

        return bfs(root, 0)


class Iterative:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            res.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                res[-1].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


class Iterative2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res


class Iterative3:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            res.append([])
            level = []
            for node in queue:
                res[-1].append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
        return res
