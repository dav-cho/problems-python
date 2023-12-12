##
#### 101. Symmetric Tree (easy)
###################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
################
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False

            outside = is_mirror(a.left, b.right)
            inside = is_mirror(a.right, b.left)

            return a.val == b.val and outside and inside

        return is_mirror(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False

            outside = helper(a.left, b.right)
            inside = helper(a.right, b.left)

            return outside and inside

        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node_a, node_b):
            if not node_a and not node_b:
                return True
            if not node_a or not node_b:
                return False
            if node_a.val != node_b.val:
                return False

            left = helper(node_a.left, node_b.right)
            right = helper(node_a.right, node_b.left)

            return left and right

        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node_a, node_b):
            if not node_a and not node_b:
                return True
            if not node_a or not node_b:
                return False

            left = helper(node_a.left, node_b.right)
            right = helper(node_a.right, node_b.left)

            return node_a.val == node_b.val and left and right

        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            left = is_mirror(node1.left, node2.right)
            right = is_mirror(node2.right, node1.left)

            return node1.val == node2.val and left and right

        return is_mirror(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False

        left = self.is_mirror(node1.left, node2.right)
        right = self.is_mirror(node2.right, node1.left)

        return node1.val == node2.val and left and right


## iterative
################
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]
        while stack:
            a, b = stack.pop()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False

            stack.append((a.left, b.right))
            stack.append((a.right, b.left))

        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]

        while stack:
            a, b = stack.pop()

            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False

            stack.append((a.left, b.right))
            stack.append((a.right, b.left))

        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]

        while stack:
            node_a, node_b = stack.pop()

            if not node_a and not node_b:
                continue
            if not node_a or not node_b:
                return False
            if node_a.val != node_b.val:
                return False

            stack.append((node_a.left, node_b.right))
            stack.append((node_a.right, node_b.left))

        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]

        while queue:
            node1 = queue.pop()
            node2 = queue.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False

            queue.append(node1.left)
            queue.append(node2.right)

            queue.append(node1.right)
            queue.append(node2.left)

        return True
