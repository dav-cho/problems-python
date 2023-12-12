##
#### 116. Populating Next Right Pointers in Each Node (medium)
###################################################################


from collections import deque


## Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


## using previously established next pointers
#################################################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
            
        return root


## level order traversal
##############################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i < size - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return root


## first attempt
##############################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        queue = [root]
        while queue:
            level = []
            for i, node in enumerate(queue):
                if i < len(queue) - 1:
                    node.next = queue[i + 1]
                else:
                    node.next = None
                    
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                    
            queue = level
            
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

