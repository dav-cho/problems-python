##
#### 426. Convert Binary Search Tree to Sorted Doubly Linked List (medium)
##############################################################################


## Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## recursive
##############################
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            nonlocal head, tail
            if tail:
                tail.right, node.left = node, tail
            else:
                head = node
            tail = node
            
            inorder(node.right)
            
        if not root:
            return
        
        head = tail = None
        inorder(root)
        head.left, tail.right = tail, head
        
        return head


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            nonlocal first, last
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            
            inorder(node.right)
            
        if not root:
            return
        
        first = last = None
        inorder(root)
        last.right = first
        first.left = last
        
        return first


## iterative
##############################
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        head = tail = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()

            if tail:
                tail.right, root.left = root, tail
            else:
                head = root
            tail = root

            root = root.right
        head.left, tail.right = tail, head
        
        return head


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()
