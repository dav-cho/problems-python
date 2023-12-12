##
#### 173. Binary Search Tree Iterator (medium)
##################################################


from typing import Optional


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## controlled recursion
##############################
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._dfs_inorder_left(root)
        
    def _dfs_inorder_left(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self._dfs_inorder_left(node.right)
        return node.val
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0


## flattening BST
##############################
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.idx = -1
        self.sorted_nodes = []
        self._dfs_inorder(root)
        
    def _dfs_inorder(self, root):
        if not root:
            return
        
        self._dfs_inorder(root.left)
        self.sorted_roots.append(root.val)
        self._dfs_inorder(root.right)

    def next(self) -> int:
        self.idx += 1
        return self.sorted_nodes[self.idx]

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.sorted_nodes)


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.idx = -1
        self.sorted_nodes = []
        self._dfs_inorder(root)
        
    def _dfs_inorder(self, root):
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            self.sorted_nodes.append(root.val)
            root = root.right

    def next(self) -> int:
        self.idx += 1
        return self.sorted_nodes[self.idx]

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.sorted_nodes)


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

