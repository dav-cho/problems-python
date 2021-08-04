##
#### Construct Binary Tree from Inorder and Postorder Traversal (medium)
############################################################################

# Given two integer arrays inorder and postorder where inorder is the inorder
# traversal of a binary tree and postorder is the postorder traversal of the
# same tree, construct and return the binary tree.

# Example 1:
#           3
#       9       20
#             15  7
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
 
# Constraints:
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder and postorder consist of unique values.
# Each value of postorder also appears in inorder.
# inorder is guaranteed to be the inorder traversal of the tree.
# postorder is guaranteed to be the postorder traversal of the tree.

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
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        inorder_map = { val: idx for idx, val in enumerate(inorder) }
        
        def helper(inorder_left_bound, inorder_right_bound):
            if inorder_left_bound > inorder_right_bound:
                return
            
            node = TreeNode(postorder.pop())
            idx = inorder_map[node.val]
            
            node.right = helper(idx + 1, inorder_right_bound)
            node.left = helper(inorder_left_bound, idx - 1)
            
            return node
        
        return helper(0, len(inorder) - 1)


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Recursion
############################
# Time: O(N) - O(N ^ (logb(a))) == O(N)
# Space: O(N) - Since we store the entire tree.
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]
 
            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root
        
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)


