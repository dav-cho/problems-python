##
#### 100. Same Tree (easy)
##############################


from typing import Optional
from collections import deque


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
##############################
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right


## iterative
##############################
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not check(p, q):
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        queue = deque([(p, q)])
        while queue:
            x, y = queue.popleft()
            if not check(x, y):
                return False

            if x:
                queue.append((x.left, y.left))
                queue.append((x.right, y.right))

        return True


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.isSameTree([1, 2, 3], [1, 2, 3]), True)
        self.assertEqual(solution.isSameTree([1, 2], [1, null, 2]), False)
        self.assertEqual(solution.isSameTree([1, 2, 1], [1, 1, 2]), False)


if __name__ == "__main__":
    unittest.main()
