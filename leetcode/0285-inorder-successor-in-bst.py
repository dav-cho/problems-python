##
#### 285. Inorder Successor in BST (medium)
###############################################



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
