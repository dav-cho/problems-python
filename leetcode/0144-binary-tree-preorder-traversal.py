##
#### Binary Tree Preorder Traversal (easy)
##############################################

# Given the root of a binary tree, return the preorder traversal of its
# nodes' values.

# Example 1:
#       1
#         2
#       3
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
#       1
#     2
# Input: root = [1,2]
# Output: [1,2]

# Example 5:
#   1
#     2
# Input: root = [1,null,2]
# Output: [1,2]
 
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?

################################################################################

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## iterations
#################
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                result.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
                
        return result


## morris traversal
#######################
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        output = []
        node = root
        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        
        return output


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: 
#################
# time: O(N) - we visit each node exactly once, thus the time complexity is
#              O(N), where N is the number of nodes, i.e. the size of tree.
# space: O(N) - depending on the tree structure, we could keep up to the
#               entire tree, therefore, the space complexity is O(N).
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return output


## Approach 2: 
#################
# time: O(N) - we visit each predecessor exactly twice descending down from
#              the node, thus the time complexity is O(N), where N is the
#              number of nodes, i.e. the size of tree.
# space: O(N) - we use no additional memory for the computation itself, but
#               output list contains N elements, and thus space complexity is
#               O(N).
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
                node = node.right 
            else: 
                predecessor = node.left 

                while predecessor.right and predecessor.right is not node: 
                    predecessor = predecessor.right 

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node  
                    node = node.left  
                else:
                    predecessor.right = None
                    node = node.right         

        return output

