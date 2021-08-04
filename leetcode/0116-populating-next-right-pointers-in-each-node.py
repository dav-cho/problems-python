##
#### Populating Next Right Pointers in Each Node (medium)
#############################################################

# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following
# definition:

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Follow up:
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not
# count as extra space for this problem.
 
# Example 1:
#        Figure A               Figure B
#           1                      1 -> null        
#       2       3             2 -------> 3 -> null     
#     4   5   6   7         4 -> 5 -> 6 -> 7 -> null
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function
# should populate each next pointer t point to its next right node, just like
# in Figure B. The serialized output is in level order as connected by the
# next pointers, with '#' signifying the end of each level.
#
# Constraints:
# The number of nodes in the given tree is less than 4096.
# -1000 <= node.val <= 1000o

################################################################################

## Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

## attempt 1
################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        levels = []
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node)
            
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        
        helper(root, 0)
        for level in levels:
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
        
        return root


## level order traversal
############################
from collections import deque

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


## using next pointers
##########################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        leftmost = root
        while leftmost.left:
            node = leftmost
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            
            leftmost = leftmost.left
            
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        curr = root
        next_curr = root.left
        while curr.left:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
            else:
                curr = next_curr
                next_curr = curr.left
        
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr and curr.left:
            next_left = curr.left
            while curr:
                curr.left.next = curr.right
                curr.right.next = curr.next and curr.next.left
                curr = curr.next
            curr = next_left
            
        return root


## recursive
################
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        curr = root
        if curr and curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            
            self.connect(root.left)
            self.connect(root.right)
        
        return root


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Level Order Traversal
########################################
# Time: O(N)
# Since we process each node exactly once. Note that processing a node in this
# context means popping the node from the queue and then establishing the next
# pointers.

# Space: O(N)
# This is a perfect binary tree which means the last level contains N / 2 nodes.# The space complexity for breadth first traversal is the space occupied by the
# queue which is dependent upon the maximum number of nodes in particular level.
# So, in this case, the space complexity would be O(N).
import collections 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])
        
        # Outer while loop which iterates over 
        # each level
        while Q:
            
            # Note the size of the queue
            size = len(Q)
            
            # Iterate over all the nodes on the current level
            for i in range(size):
                
                # Pop a node from the front of the queue
                node = Q.popleft()
                
                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only 
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]
                
                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # Since the tree has now been modified, return the root node
        return root


## Approach 2: Using previously established next pointers
#############################################################
# Time: O(N) - Since we process each node exactly once.
# Space: O(1) - Since we don't make use of any additional data structure for
#               traversing nodes on a particular level like the previous
#               approach does.
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root

