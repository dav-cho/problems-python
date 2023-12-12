##
#### 117. Populating Next Right Pointers in Each Node II (medium)
#####################################################################


## Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


## using populated next pointers
####################################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        leftmost = root
        while leftmost:
            prev = None
            curr = leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)
                curr = curr.next
                
        return root
    
    def process_child(self, child, prev, leftmost):
        if child:
            if prev:
                prev.next = child
            else:
                leftmost = child
            prev = child
        
        return prev, leftmost


## level order
##############################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        queue = deque([root])
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


## first attempt using populated next pointers
##################################################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pass


## first attempt level order (bfs)
######################################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        queue = deque([root])
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

