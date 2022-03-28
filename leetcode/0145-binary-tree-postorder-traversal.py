##
#### 145. Binary Tree Postorder Traversal (easy)
####################################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
################
class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        res = []

        def dfs_postorder(node):
            if not node:
                return

            dfs_postorder(node.left)
            dfs_postorder(node.right)
            res.append(node.val)

            return res

        return dfs_postorder(root)


class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        return self.dfs_postorder(root, [])

    def dfs_postorder(self, node, res):
        if not node:
            return

        self.dfs_postorder(node.left, res)
        self.dfs_postorder(node.right, res)
        res.append(node.val)

        return res


class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if not node:
            return

        self.helper(node.left, result)
        self.helper(node.right, result)
        result.append(node.val)


## iterative
################
class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue

            res.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

        return res[::-1]


class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        stack = [(root, False)]
        while stack:
            node, seen = stack.pop()
            if not node:
                continue

            if seen:
                res.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return res


class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.right

            root = stack.pop()
            root = root.left

        return reversed(res)


from collections import deque


class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        result, stack = deque([]), []
        while stack or root:
            while root:
                result.appendleft(root.val)
                stack.append(root)
                root = root.right

            root = stack.pop()
            root = root.left

        return result


## morris traversal
#######################
class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        result = []
        while root:
            if not root.right:
                result.append(root.val)
                root = root.left
            else:
                pred = root.right

                while pred.left and pred.left is not root:
                    pred = pred.left

                if not pred.left:
                    result.append(root.val)
                    pred.left = root
                    root = root.right
                else:
                    pred.left = None
                    root = root.left

        return reversed(result)
