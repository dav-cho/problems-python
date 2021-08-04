##
#### Construct Binary Tree from Preorder and Inorder Traversal (medium)
###########################################################################

# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.

# Example 1:
#           3
#       9       20
#            15    7
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 
# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

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
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        preorder.reverse()
        inorder_map = { val: idx for idx, val in enumerate(inorder) }
        
        def helper(preorder_left_bound, preorder_right_bound):
            if preorder_left_bound > preorder_right_bound:
                return
            
            node = TreeNode(preorder.pop())
            idx = inorder_map[node.val]
            
            node.left = helper(preorder_left_bound, idx - 1)
            node.right = helper(idx + 1, preorder_right_bound)
            
            return node
        
        return helper(0, len(preorder) - 1)


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        preorder_idx = 0
        inorder_map = { val: idx for idx, val in enumerate(inorder) }
        
        def helper(inorder_left_bound, inorder_right_bound):
            if inorder_left_bound > inorder_right_bound:
                return
            
            nonlocal preorder_idx
            root = TreeNode(preorder[preorder_idx])
            idx = inorder_map[root.val]
            preorder_idx += 1
            
            root.left = helper(inorder_left_bound, idx - 1)
            root.right = helper(idx + 1, inorder_right_bound)
            
            return root
        
        return helper(0, len(preorder) - 1)


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        preorder_idx = 0
        inorder_map = { val: idx for idx, val in enumerate(inorder) }

        def helper(inorder_left_bound, inorder_right_bound):
            if inorder_left_bound > inorder_right_bound:
                return
            
            nonlocal preorder_idx
            root = TreeNode(preorder[preorder_idx])
            idx = inorder_map[root.val]
            preorder_idx += 1
            
            root.left = helper(inorder_left_bound, idx - 1)
            root.right = helper(idx + 1, inorder_right_bound)
            
            return root
        
        return helper(0, len(preorder) - 1)


## O(N ^ 2) (do not use)
############################
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not inorder:
            return

        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[0:idx])
        root.right = self.buildTree(preorder, inorder[idx + 1:])

        return root


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Recursion
############################
# Time: O(N)
# - Building the hashmap takes O(N) time, as there are N nodes to add, and
#   adding items to a hashmap has a cost of O(1), so we get N * O(1) = O(N).
# - Building the tree also takes O(N) time. The recursive helper method has a
#   cost of O(1) for each call (it has no loops), and it is called once for each
#   of the N nodes, giving a total of O(N).
# - Taking both into consideration, the time complexity is O(N).
# Space: O(N)
# - Building the hashmap and storing the entire tree each requires O(N) memory.
#   The size of the implicit system stack used by recursion calls depends on the
#   height of the tree, which is O(N) in the worst case and O(logN) on average.
#   Taking both into consideration, the space complexity is O(N).
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)


