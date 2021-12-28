##
#### Search in a Binary Search Tree (easy)
##############################################

# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.

# Example 1:

# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]

# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107

################################################################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
##############################
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)


## iterative
##############################
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
            
        return root


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            root = root.left if val < root.val else root.right
            
        return root


## first attempt
##############################
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val == val:
            return root
        
        left = self.searchBST(root.left, val)
        if left and left.val == val:
            return left
        
        right = self.searchBST(root.right, val)
        if right and right.val == val:
            return right
        
        return None


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursion
############################
# Time: O(H)
# Where H is a tree height. That results in O(logN) in the average case, and
# O(N) in the worst case.

# Let's compute time complexity with the help of master theorem
# T(N)=aT(b/N)+Θ(N^d). The equation represents dividing the problem up into a
# subproblems of size N/b in Θ(N^d) time. Here at step there is only one
# subproblem a = 1, its size is a half of the initial problem b = 2, and all
# this happens in a constant time d = 0, as for the binary search. That means
# that logb(a)=d and hence we're dealing with case 2
# that results in O(n^(logb(a)) * log^(d+1) * N) = O(logN) time complexity.

# Space: O(H)
# O(H) to keep the recursion stack, i.e. O(logN) in the average case, and
# O(N) in the worst case.
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)


## Approach 2: Iteration
############################
# Time: O(H)
# Where H is a tree height. That results in O(logN) in the average case, and
# O(N) in the worst case.

# Let's compute time complexity with the help of master theorem
# T(N)=aT(b/N)+Θ(N^d). The equation represents dividing the problem up into a
# subproblems of size N/b in Θ(N^d) time. Here at step there is only one
# subproblem a = 1, its size is a half of the initial problem b = 2, and all
# this happens in a constant time d = 0, as for the binary search. That means
# that logb(a)=d and hence we're dealing with case 2
# that results in O(n^(logb(a)) * log^(d+1) * N) = O(logN) time complexity.

# Space: O(1)
# Since it's a constant space solution.
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root


