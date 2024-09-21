"""
145. Binary Tree Postorder Traversal (easy)
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursive:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return res
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
            return res

        return dfs(root)


class IterativeModifiedPreOrder:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return reversed(res)


class IterativeBest:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack: List[TreeNode] = []
        while stack or root:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if stack and root.right and stack[-1] is root.right:
                stack[-1], root = root, root.right
                continue
            res.append(root.val)
            root = None
        return res


class Iterative:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        node = root
        while stack or node:
            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            node = stack.pop()
            if stack and node.right and stack[-1] is node.right:
                stack[-1] = node
                node = node.right
                continue
            res.append(node.val)
            node = None
        return res


class Iterative2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.right and stack and stack[-1] is node.right:
                stack.pop()
                stack.append(node)
                node = node.right
                continue
            res.append(node.val)
            node = None
        return res


class Itarative3:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while stack or root:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if stack and root.right and stack[-1] is root.right:
                stack[-1] = root
                root = root.right
                continue
            res.append(root.val)
            root = None
        return res
