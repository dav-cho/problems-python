##
#### Balanced Binary Tree (easy)
########################################

# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:
#   A binary tree in which the left and right subtrees of every node differ in
#   height by no more than 1.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true
 
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

################################################################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## top-down recursion
##############################
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        check_height = abs(self.height(root.left) - self.height(root.right)) < 2
        check_left = self.isBalanced(root.left)
        check_right = self.isBalanced(root.right)
        
        return check_height and check_left and check_right
    
    def height(self, root):
        if not root:
            return -1
        
        return 1 + max(self.height(root.left), self.height(root.right))


## bottom-up recursion
##############################
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return True, -1
            
            left_balanced, left_height = helper(node.left)
            
            if not left_balanced:
                return False, 0
            
            right_balanced, right_height = helper(node.right)
            
            if not right_balanced:
                return False, 0
            
            check_height = abs(left_height - right_height) < 2
            height = 1 + max(left_height, right_height)
            
            return check_height, height
        
        return helper(root)[0]


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return True, -1
            
            left_balanced, left_height = helper(node.left)
            right_balanced, right_height = helper(node.right)
            
            if not left_balanced:
                return False, 0
            if not right_balanced:
                return False, 0
            
            check_height = abs(left_height - right_height) < 2
            max_height = 1 + max(left_height, right_height)
            
            return check_height, max_height
        
        return helper(root)[0]


## 
##############################
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        pass


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

## Approach 1: Top-down Recursion
#####################################
# Time: O(nlogn)
# - For a node p at depth d, height(p) will be called d times.
# - We first need to obtain a bound on the height of a balanced tree. Let f(h)
#   represent the minimum number of nodes in a balanced tree with height h. We
#   have the relation
#       f(h) = f(h - 1) + f(h - 2) + 1f(h)=f(h−1)+f(h−2)+1
#   which looks nearly identical to the Fibonacci recurrence relation. In fact,
#   the complexity analysis for f(h) is similar and we claim that the lower
#   bound is f(h) = Ω((3/2)^h).

#       f(h+1) = f(h) + f(h-1) + 1
#              > f(h) + f(h-1)                # This is the fibonacci sequence
#              ≥ (3/2)^h + (3/2)^(h-1)        # via our claim
#              = (5/2)(3/2)^(h-1)
#              > (9/4)(3/2)^(h-1)             # (9/4) < (5/2)
#              > (3/2)^(h+1)

# Therefore, the height h of a balanced tree is bounded by O(log_1.5(n)). With
# this bound we can guarantee that height will be called on each node
# O(logn) times.
# - If our algorithm didn't have any early-stopping, we may end up having
#   O(n^2) complexity if our tree is skewed since height is bounded by O(n).
#   However, it is important to note that we stop recursion as soon as the
#   height of a node's children are not within 1. In fact, in the skewed-tree
#   case our algorithm is bounded by O(n), as it only checks the height of the
#   first two subtrees.

# Space: O(n)
# - The recursion stack may contain all nodes if the tree is skewed.

class Solution:
    # Compute the tree's height via recursion
    def height(self, root: TreeNode) -> int:
        # An empty tree has height -1
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def isBalanced(self, root: TreeNode) -> bool:
        # An empty tree satisfies the definition of a balanced tree
        if not root:
            return True

        # Check if subtrees have height within 1. If they do, check if the
        # subtrees are balanced
        return abs(self.height(root.left) - self.height(root.right)) < 2 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)



## Approach 2: Bottom-up Recursion
######################################
# Time: O(n) - For every subtree, we compute its height in constant time as
#              well as compare the height of its children
# Space: O(n) - The recursion stack may go up to O(n) if the tree is unbalanced.
class Solution:
    # Return whether or not the tree at root is balanced while also returning
    # the tree's height
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
        
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


