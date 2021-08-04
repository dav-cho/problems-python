##
#### Count Univalue Subtrees (medium)
#########################################

# Given the root of a binary tree, return the number of uni-value subtrees.

# A uni-value subtree means all nodes of the subtree have the same value.

# Example 1:
# Input: root = [5,1,5,5,5,null,5]
# Output: 4

# Example 2:
# Input: root = []
# Output: 0

# Example 3:
# Input: root = [5,5,5,5,5,null,5]
# Output: 6
 
# Constraints:
# The numbrt of the node in the tree will be in the range [0, 1000].
# -1000 <= Node.val <= 1000

################################################################################

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## dfs recursive
####################
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.count = 0
        self.check_uni(root)
        return self.count
    
    def check_uni(self, node):
        if not node.left and not node.right:
            self.count += 1
            return True
        
        is_uni = True
        
        if node.left:
            is_uni = self.check_uni(node.left) and is_uni and node.left.val == node.val
        if  node.right:
            is_uni = self.check_uni(node.right) and is_uni and node.right.val == node.val
            
        self.count += is_uni
        return is_uni


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.check_uni(root)
        return self.count
    
    def check_uni(self, node):
        if not node:
            return True
        
        left = self.check_uni(node.left)
        right = self.check_uni(node.right)
        left_check = not node.left or node.left.val == node.val
        right_check = not node.right or node.right.val == node.val
        
        if left and right and left_check and right_check:
            self.count += 1
            return True
        
        return False


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.check_uni(root)
        
        return self.count
    
    def check_unival(self, node):
        if not node:
            return True
        
        left = self.check_unival(node.left)
        right = self.check_unival(node.right)
        left_check = not node.left or node.left.val == node.val
        right_check = not node.right or node.right.val == node.val

        if all([left, right, left_check, right_check]):
            self.count += 1
            return True
        
        return False


## dfs passing parent values
################################
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.check_unival(root, None)
        return self.count
    
    def check_unival(self, node, val):
        if not node:
            return True
        
        left = self.check_unival(node.left, node.val)
        right = self.check_unival(node.right, node.val)
        if not left or not right:
            return False
        
        self.count += 1
        
        return node.val == val


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        
        def helper(node):
            if not node:
                return
            
            left = helper(node.left)
            right = helper(node.right)
            left_check = not left or left == node.val
            right_check = not right or right == node.val
            
            if left_check and right_check:
                self.count += 1
                return node.val
            
            return "dav"
        
        helper(root)
        return self.count


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Depth First Search
#####################################
# Time: O(n)
# Due to the algorithm's depth-first nature, the is_uni status of each node is
# computed from bottom up. When given the is_uni status of its children,
# computing the is_uni status of a node occurs in O(1).

# This gives us O(1) time for each node in the tree with O(N) total nodes for a
# time complexity of O(N).

# Space: O(H)
# With H being the height of the tree. Each recursive call of is_uni requires
# stack space. Since we fully process is_uni(node.left) before calling
# is_uni(node.right), the recursive stack is bound by the longest path from the
# root to a leaf - in other words the height of the tree.
class Solution:
    def countUnivalSubtrees(self, root):
        if root is None: return 0
        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):

        # base case - if the node has no children this is a univalue subtree
        if node.left is None and node.right is None:

            # found a univalue subtree - increment
            self.count += 1
            return True

        is_uni = True

        # check if all of the node's children are univalue subtrees and if they have the same value
        # also recursively call is_uni for children
        if node.left is not None:
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val

        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        # increment self.res and return whether a univalue tree exists here
        self.count += is_uni
        return is_uni


## Approach 2: Depth First Search - Pass Parent Values
##########################################################
# Time: O(n) - Same as previous approach.
# Space: O(H) - with H being the height of the tree. Same as previous appraoch.
class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count


    def is_valid_part(self, node, val):

        # considered a valid subtree
        if node is None: return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.val),
                    self.is_valid_part(node.right, node.val)]):
            return False

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val

