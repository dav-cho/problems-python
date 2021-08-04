##
#### Binary Tree Postorder Traversal (easy)
###############################################

# Given the root of a binary tree, return the postorder traversal of its
# nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
# Input: root = [1,2]
# Output: [2,1]

# Example 5:
# Input: root = [1,null,2]
# Output: [2,1]
 
# Constraints:
# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 
# Follow up: Recursive solution is trivial, could you do it iteratively?

################################################################################

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
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, node, result):
        if not node:
            return
        
        self.helper(node.left, result)
        self.helper(node.right, result)
        result.append(node.val)


class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        def helper(node, result):
            if not node:
                return
            
            helper(node.left, result)
            helper(node.right, result)
            result.append(node.val)
            
            return result
        
        return helper(root, [])


class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        if not root:
            return

        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        left = left if left else []
        right = right if right else []

        return left + right + [root.val]


## iterative
################
class Solution:
    def postorder_traversal(self, root: TreeNode) -> list[int]:
        result, stack = [], []
        while stack or root:
            while root:
                result.append(root.val)
                stack.append(root)
                root = root.right
                
            root = stack.pop()
            root = root.left
            
        return reversed(result)


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


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Rescursive
#############################
# time: 
# space: 


## Approach 2: Iterative
############################
# time: 
# space: 


## Approach 3: Morris Traversal
###################################
# time: 
# space: 


