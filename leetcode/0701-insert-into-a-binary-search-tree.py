##
#### Insert into a Binary Search Tree (medium)
##################################################

# You are given the root node of a binary search tree (BST) and a value to
# insert into the tree. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long
# as the tree remains a BST after insertion. You can return any of them.

# Example 1:
#       4            4
#    2     7      2     7 
#   1 3          1 3  (5)   
# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:
#           5
#       2       7
#     1   3   
#          4
# Example 2:
# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]

# Example 3:
# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
 
# Constraints:
# The number of nodes in the tree will be in the range [0, 104].
# -108 <= Node.val <= 108
# All the values Node.val are unique.
# -108 <= val <= 108
# It's guaranteed that val does not exist in the original BST.

################################################################################

from typing import Optinal


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
##############################
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
            
        return root


## iterative
##############################
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
                    
        return TreeNode(val)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )
        self.assertCountEqual()


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursion
##############################
# Time: O(H) -  Where H is a tree height. That results in O(logN) in the average
#               case, and O(N) in the worst case.
# - Let's compute time complexity with the help of master theorem
#   T(N) = aT(b/N) + Θ(N^d). The equation represents dividing the problem up
#   into a subproblems of size N/b in Θ(N^d) time. Here at step there is only
#   one subproblem a = 1, its size is a half of the initial problem b = 2, and
#   all this happens in a constant time d = 0, as for the binary search. That
#   means that log_b(a) = d and hence we're dealing with case 2 that results in
#   O(n^(log_b(a)) * log(d+1) * N) = O(log(N)) time complexity.

# Space: O(H) - To keep the recursion stack, i.e. O(logN) in the average case,
#               and O(N) in the worst case.
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            # insert into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # insert into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root


## Approach 2: Iteration
##############################
# Time: O(H) - Same as approach 1.
# Space: O(1) - Since it's a constant space solution.
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node:
            # insert into the right subtree
            if val > node.val:
                # insert right now
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            # insert into the left subtree
            else:
                # insert right now
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
        return TreeNode(val)


## Approach 3: 
##############################
# Time: 
# Space: 


