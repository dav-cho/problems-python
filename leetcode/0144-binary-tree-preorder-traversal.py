##
#### Binary Tree Preorde Traversal (easy)
#############################################

# Given the root of a binary tree, return the preorder traversal of its
# nodes' values.

# Example 1:
#   1
#     2
#   3
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]
 
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

################################################################################

from typing import Optional


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
##############################
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        
        def dfs_preorder(node):
            if not node:
                return
            
            res.append(node.val)
            dfs_preorder(node.left)
            dfs_preorder(node.right)
            
            return res
        
        return dfs_preorder(root)


## iterative
##############################
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
                
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
            
        return res


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return res


## morris traversal
##############################
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        node = root
        while node:
            if not node.left:
                res.append(node.val)
                node = node.right
            else:
                leaf = node.left
                
                while leaf.right and leaf.right is not node:
                    leaf = leaf.right
                    
                if not leaf.right:
                    res.append(node.val)
                    leaf.right = node
                    node = node.left
                else:
                    leaf.right = None
                    node = node.right
        return res


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        node = root
        while node:
            if not node.left:
                res.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right
                    
                if not predecessor.right:
                    res.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().preorderTraversal([1,None,2,3]), [1,2,3])
        self.assertEqual(Solution().preorderTraversal([]), [])
        self.assertEqual(Solution().preorderTraversal([1]), [1])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Iterations
##############################
# Time: O(N) - We visit each node exactly once, thus the time complexity is
#              O(N), where N is the number of nodes, i.e. the size of tree.
# Space: O(N) - Depending on the tree structure, we could keep up to the entire
#               tree, therefore, the space complexity is O(N).
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


## Approach 2: Morris Traversal
###################################
# Time: O(N) - We visit each predecessor exactly twice descending down from the
#              node, thus the time complexity is O(N), where N is the number
#              of nodes, i.e. the size of tree.
# Space: O(N) - We use no additional memory for the computation itself, but
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


