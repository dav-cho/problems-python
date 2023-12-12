##
#### 250. Count Univalue Subtrees (medium)
##############################################


from typing import Optional


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## dfs - passing parent values
##################################
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count

    def is_valid_part(self, node, val):
        if not node:
            return True

        left = self.is_valid_part(node.left, node.val)
        right = self.is_valid_part(node.right, node.val)
        if not all((left, right)):
            return False

        self.count += 1
        return node.val == val


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def is_valid_part(node, val):
            if not node:
                return True

            left = is_valid_part(node.left, node.val)
            right = is_valid_part(node.right, node.val)
            if not (left and right):
                return False

            self.count += 1

            return node.val == val

        self.count = 0
        is_valid_part(root, 0)

        return self.count


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count

    def is_valid_part(self, node, val):
        if not node:
            return True

        left = self.is_valid_part(node.left, node.val)
        right = self.is_valid_part(node.right, node.val)
        if not (left and right):
            return False

        self.count += 1

        return node.val == val


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count

    def is_valid_part(self, node, val):
        if not node:
            return True

        left = self.is_valid_part(node.left, node.val)
        right = self.is_valid_part(node.right, node.val)
        if not left or not right:
            return False

        self.count += 1

        return node.val == val


## dfs
##############################
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.count = 0
        self.is_uni(root)

        return self.count

    def is_uni(self, node):
        if not node.left and not node.right:
            self.count += 1
            return True

        is_uni = True
        if node.left:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val
        if node.right:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        self.count += is_uni
        return is_uni


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def is_uni(node):
            if not node.left and not node.right:
                self.count += 1
                return True

            ans = True
            if node.left:
                ans = is_uni(node.left) and ans and node.left.val == node.val
            if node.right:
                ans = is_uni(node.right) and ans and node.right.val == node.val

            self.count += ans
            return ans

        self.count = 0
        is_uni(root)

        return self.count


##
##############################
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().countUnivalSubtrees([5, 1, 5, 5, 5, None, 5]), 4)
        self.assertEqual(Solution().countUnivalSubtrees([]), 0)
        self.assertEqual(Solution().countUnivalSubtrees([5, 5, 5, 5, 5, None, 5]), 6)


if __name__ == "__main__":
    unittest.main()
