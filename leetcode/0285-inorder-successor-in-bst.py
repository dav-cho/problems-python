##
#### Inorder Successor in BST (medium)
##########################################

# Given the root of a binary search tree and a node p in it, return the
# in-order successor of that node in the BST. If the given node has no in-order
# successor in the tree, return null.

# The successor of a node p is the node with the smallest key
# greater than p.val.

# Example 1:
#     2
#   1   3
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

# Example 2:
#           5
#       3       6
#     2   4
#   1
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.
 
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
# All Nodes will have unique values.

################################################################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


## using bst properties
##############################
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        successor = None
        
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        successor = None
        
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor


## without bst properties (any binary tree)
###############################################
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        self.prev = None
        self.successor = None
        
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
            self.successor = leftmost
        else:
            self.inorder_case2(root, p)
            
        return self.successor
    
    def inorder_case2(self, node, p):
        if not node:
            return
        
        self.inorder_case2(node.left, p)

        if self.prev == p and not self.successor:
            self.successor = node
            return
        
        self.prev = node
        self.inorder_case2(node.right, p)


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        self.prev = None
        self.successor = None
        
        if p.right:
            leftmost = p.right
            
            while leftmost.left:
                leftmost = leftmost.left
                
            self.successor = leftmost
        else:
            self.dfs_inorder(root, p)
            
        return self.successor
        
    def dfs_inorder(self, node, p):
        stack = []
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            
            if self.prev == p and not self.successor:
                self.successor = node
                return
            
            self.prev = node
            node = node.right


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        self.prev = None
        self.successor = None
        
        def dfs_inorder(node):
            if not node:
                return
            
            dfs_inorder(node.left)
            
            if self.prev == p and not self.successor:
                self.successor = node
            
            self.prev = node
            dfs_inorder(node.right)
        
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
            self.successor = leftmost
        else:
            dfs_inorder(root)
            
        return self.successor


## dfs inorder traversal
##############################
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        self.prev = None
        self.successor = None
        
        def dfs_inorder(node):
            if not node:
                return
            
            dfs_inorder(node.left)
            
            if self.prev == p and not self.successor:
                self.successor = node
            
            self.prev = node
            dfs_inorder(node.right)
            
            return self.successor
        
        return dfs_inorder(root)


class Solution:
    def __init__(self):
        self.prev = None
        self.successor = None
        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        if not root:
            return
        
        self.inorderSuccessor(root.left, p)
        
        if self.prev == p and not self.successor:
            self.successor = root
        
        self.prev = root
        self.inorderSuccessor(root.right, p)
        
        return self.successor


## first attempt
##############################
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        def dfs_inorder(node, nodes):
            if not node:
                return
            
            dfs_inorder(node.left, nodes)
            nodes.append(node)
            dfs_inorder(node.right, nodes)
            
            return nodes
            
        nodes = dfs_inorder(root, [])
        for i in range(len(nodes) - 1):
            if nodes[i] == p:
                return nodes[i + 1]
            
        return None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        nodes = []
        
        def dfs_inorder(node):
            if not node:
                return
            
            dfs_inorder(node.left)
            nodes.append(node)
            dfs_inorder(node.right)
            
        dfs_inorder(root)
        for i in range(len(nodes) - 1):
            if nodes[i] is p:
                return nodes[i + 1]
            
        return


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

## Approach 1: Without using BST properties
###############################################
# Time: O(N) - Where N is the number of nodes in the tree.
# - Case 1:
#   - We might have a scenario where the root node has a right subtree that is
#     left-skewed. Something like the following.
#          (6)
#             10
#           9
#         8
#      [7]
#   - This is an extremely skewed tree and in this case, we will find our
#     inorder successor after processing all the nodes in the tree thus giving
#     us our worst-case complexity of O(N).
#   - In this case, we have to process all of the nodes to find the leftmost
#     node and hence, the overall time complexity is O(N).
# - Case 2:
#   - We might have to process the entire tree before finding the inorder
#     successor. Let's look at an example tree to understand when that
#     might happen.
#        [6]  
#       2
#         3   
#           4 
#            (5)
#   - This is an extremely skewed tree and in this case, we will find our
#     inorder successor after processing all the nodes in the tree thus giving
#     us our worst-case complexity of O(N)

# Space: O(N)
# - For the second case since we might have a skewed tree leading to a
#   recursion stack containing all N nodes. For the first case, we don't have
#   any additional space complexity since we simply use a while loop to find
#   the successor.
class Solution:
    
    previous = None
    inorder_successor_node = None
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        self.previous, self.inorder_successor_node = None, None
        
        # Case 1: We simply need to find the leftmost node in the subtree rooted at p.right.
        if p.right:
            leftmost = p.right
            while leftmost.left:
                leftmost = leftmost.left
                
            self.inorder_successor_node = leftmost
        
        # Case 2: We need to perform the standard inorder traversal and keep track of the previous node.
        else:
            self.inorderCase2(root, p)
        
        return self.inorder_successor_node
        
        
    def inorderCase2(self, node: 'TreeNode', p: 'TreeNode'):
        
        if not node:
            return
        
        # Recurse on the left side
        self.inorderCase2(node.left, p)
        
        # Check if previous is the inorder predecessor of node
        if self.previous == p and not self.inorder_successor_node:
            self.inorder_successor_node = node
            return
        
        # Keeping previous up-to-date for further recursions
        self.previous = node
        
        # Recurse on the right side
        self.inorderCase2(node.right, p)


## Approach 2: Using BST properties
#######################################
# Time: O(N) - Since we might end up encountering a skewed tree and in that
#              case, we will just be discarding one node at a time. For a
#              balanced binary-search tree, however, the time complexity will
#              be O(logN) which is what we usually find in practice.
# Space: O(1) - Since we don't use recursion or any other data structures for
#               getting our successor.
class Solution:
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        successor = None
        
        while root:
            
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
                
        return successor


