##
#### 94. Binary Tree Inorder Traversal (easy)
#################################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
################
class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        res = []

        def dfs_inorder(node):
            if not node:
                return

            dfs_inorder(node.left)
            res.append(node.val)
            dfs_inorder(node.right)

            return res

        return dfs_inorder(root)


class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        return self.dfs_inorder(root, [])

    def dfs_inorder(self, node, res):
        if not node:
            return

        self.dfs_inorder(node.left, res)
        res.append(node.val)
        self.dfs_inorder(node.right, res)

        return res


class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if not node:
            return

        self.helper(node.left, res)
        res.append(node.val)
        self.helper(node.right, res)


## iterative
################
class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res


class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            res.append(node.val)
            root = node.right

        return res


class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            res.append(node.val)
            node = node.right

        return res


## morris traversal
#######################
class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        res = []
        while root:
            if not root.left:
                res.append(root.val)
                root = root.right
            else:
                leaf = root.left

                while leaf.right:
                    leaf = leaf.right

                leaf.right = root
                root.left, root = None, root.left

        return res


class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        result = []
        while root:
            if not root.left:
                result.append(root.val)
                root = root.right
            else:
                pred = root.left

                while pred.right:
                    pred = pred.right

                pred.right = root
                root.left, root = None, root.left

        return result


## Tests
############
