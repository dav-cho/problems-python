##
#### Path Sum (easy)
########################

# Given the root of a binary tree and an integer targetSum, return true if the
# tree has a root-to-leaf path such that adding up all the values along the path# equals targetSum.

# A leaf is a node with no children.

# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false

# Example 3:
# Input: root = [1,2], targetSum = 0
# Output: false
 
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

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
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0

        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)
        
        return left or right


## iterative
################
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        queue = [(root, targetSum - root.val)]
        while queue:
            node, curr_sum = queue.pop()

            if not node.left and not node.right and curr_sum == 0:
                return True

            if node.left:
                queue.append((node.left, curr_sum - node.left.val))
            if node.right:
                queue.append((node.right, curr_sum - node.right.val))
                
        return False


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Recursion
############################
# Time: O(N) - We visit each node exactly once, thus the time complexity is
#              O(N), where N is the number of nodes.
# Space: O(N) - In the worst case, the tree is completely unbalanced, e.g. each
#               node has only one child node, the recursion call would occur N
#               times (the height of the tree), therefore the storage to keep
#               the call stack would be O(N). But in the best case (the tree is
#               completely balanced), the height of the tree would be log(N).
#               Therefore, the space complexity in this case would be O(log(N)).
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


## Approach 2: Iterations
#############################
# Time: O(N) - The same as the recursion approach.
# Space: O(N) - since in the worst case, when the tree is completely unbalanced,#               e.g. each node has only one child node, we would keep all N
#               nodes in the stack. But in the best case (the tree is balanced),#               the height of the tree would be log(N). Therefore, the space
#               complexity in this case would be O(log(N)).
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False


