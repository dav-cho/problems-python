##
#### Same Tree (easy)
#########################

# Given the roots of two binary trees p and q, write a function to check if they
# are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 
# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

################################################################################

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
        self.assertEqual(solution.isSameTree([1,2,3], [1,2,3]), True)
        self.assertEqual(solution.isSameTree([1,2], [1,null,2]), False)
        self.assertEqual(solution.isSameTree([1,2,1], [1,1,2]), False)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursion
############################
# Time: O(N) -  Where N is a number of nodes in the tree, since one visits each
#               node exactly once.
# Space: O(log(N)) - In the best case of completely balanced tree and O(N) in
#                    the worst case of completely unbalanced tree, to keep a
#                    recursion stack.
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)


## Approach 2: Iteration
############################
# Time: O(N) - Since each node is visited exactly once.
# Space: O(log(N)) - In the best case of completely balanced tree and O(N) in
#                    the worst case of completely unbalanced tree, to keep a
#                    deque.
from collections import deque
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
                    
        return True


