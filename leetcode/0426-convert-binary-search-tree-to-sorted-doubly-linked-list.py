##
#### Convert Binary Search Tree to Sorted Doubly Linked List (medium)
#########################################################################

# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

# You can think of the left and right pointers as synonymous to the predecessor
# and successor pointers in a doubly-linked list. For a circular doubly linked
# list, the predecessor of the first element is the last element, and the
# successor of the last element is the first element.

# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

# Example 1:
# Input: root = [4,2,5,1,3]
# Output: [1,2,3,4,5]
# Explanation: The figure below shows the transformed BST. The solid line
#              indicates the successor relationship, while the dashed line means
#              the predecessor relationship.

# Example 2:
# Input: root = [2,1,3]
# Output: [1,2,3]

# Example 3:
# Input: root = []
# Output: []
# Explanation: Input is an empty tree. Output is also an empty Linked List.

# Example 4:
# Input: root = [1]
# Output: [1]
 
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
# All the values of the tree are unique.

################################################################################

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


## LeetCode Solutions
#########################

## Approach 1: Recursion
##############################
# Time: O(N) - Since each node is processed exactly once.
# Space: O(N) - We have to keep a recursion stack of the size of the tree
#               height, which is O(logN) for the best case of completely
#               balanced tree and O(N) for the worst case of completely
#               unbalanced tree.
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node
                # right
                helper(node.right)
        
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last
        return first


