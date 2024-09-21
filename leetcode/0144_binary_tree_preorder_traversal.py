"""
144. Binary Tree Preorde Traversal (easy)
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursive:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return res
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return res

        return dfs(root)


class Iteative:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class MorrisTraversal:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        node = root
        while node:
            if not node.left:
                res.append(node.val)
                node = node.right
            else:
                pred = node.left
                while pred.right and pred.right is not node:
                    pred = pred.right
                if not pred.right:
                    res.append(node.val)
                    pred.right = node
                    node = node.left
                else:
                    pred.right = None
                    node = node.right
        return res


class MorrisTraversal2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
                continue
            leaf = root.left
            while leaf.right and leaf.right is not root:
                leaf = leaf.right
            if not leaf.right:
                res.append(root.val)
                leaf.right = root
                root = root.left
                continue
            leaf.right = None
            root = root.right
        return res


class MorrisTraversal3:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                leaf = root.left
                while leaf.right and leaf.right is not root:
                    leaf = leaf.right
                if not leaf.right:
                    res.append(root.val)
                    leaf.right = root
                    root = root.left
                else:
                    leaf.right = None
                    root = root.right
        return res
