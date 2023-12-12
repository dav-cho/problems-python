##
#### 450. Delete Node in a BST (medium)
###########################################


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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                
        return root
    
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val


## wip
##############################
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pass
    
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + inorder(root.right) if root else []
    
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root


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
