##
#### Validate Binar Search Tree (medium)
############################################

# Given the root of a binary tree, determine
# if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with
# keys less than the node's key.
# The right subtree of a node contains only nodes with
# keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Example 1:
# Input: root = [2,1,3]
# Output: true

# Example 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

###############################################################################

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## dfs valid range recursive
##############################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            if not low < node.val < high:
                return False
            
            left = helper(node.left, low, node.val)
            right = helper(node.right, node.val, high)
            
            return left and right
        
        return helper(root)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            left = validate(node.left, low, node.val)
            right = validate(node.right, node.val, high)
            return left and right
        
        return validate(root)


## dfs valid range iterative
##############################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, low, high = stack.pop()
            
            if not node:
                continue
            
            if not low < node.val < high:
                return False
            
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
                
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, low, high = stack.pop()
            
            if not low < node.val < high:
                return False
            
            if node.left:
                stack.append((node.left, low, node.val))
            if node.right:
                stack.append((node.right, node.val, high))
                
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if node.val <= low or node.val >= high:
                return False
                
            stack.append((node.left, low, node.val))
            stack.append((node.right, node.val, high))
        
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if node.val <= low or node.val >= high:
                return False
                
            if node.left:
                stack.append((node.left, low, node.val))
            if node.right:
                stack.append((node.right, node.val, high))
        
        return True


## inorder recursive
##############################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        vals = []
        
        def dfs_inorder(node):
            if not node:
                return
            
            dfs_inorder(node.left)
            vals.append(node.val)
            dfs_inorder(node.right)
            
        dfs_inorder(root)
        
        for i in range(1, len(vals)):
            if vals[i] <= vals[i - 1]:
                return False
            
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            
            self.prev = root.val
            return inorder(root.right)
        
        self.prev = float('-inf')
        return inorder(root)


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            
            self.prev = node.val
            return inorder(node.right)
        
        self.prev = float('-inf')
        return inorder(root)


## inorder iterative
##############################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        prev = float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            
            if root.val <= prev:
                return False
            
            prev = root.val
            root = root.right
            
        return True


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

## Approach 1: Recursive Traversal with Valid Range
#######################################################
# Time: O(N) - Since we visit each node exactly once.
# Space: O(N) - Since we keep up to the entire tree.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))

        return validate(root)


## Approach 2: Iterative Traversal with Valid Range
#######################################################
# Time: O(N) - Since we visit each node exactly once.
# Space: O(N) - Since we keep up to the entire tree.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


## Approach 3: Recursive Inorder Traversal
##############################################
# Time: O(N) - In the worst case when the tree is a BST or the "bad" element is
#              a rightmost leaf.
# Space: O(N) - For the space on the run-time stack.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)


## Approach 4: Iterative Inorder Traversal
##############################################
# Time: O(N) - In the worst case when the tree is a BST or the "bad" element is
#              a rightmost leaf.
# Space: O(N) - To keep the stack.
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
