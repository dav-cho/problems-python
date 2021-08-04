##
#### Populating Next Right Pointers in Each Node II (medium)
################################################################

# Given a binary tree

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
#           1                      1 -> null        
#       2       3             2 -------> 3 -> null     
#     4   5       7         4 -> 5 ------> 7 -> null
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.

# Constraints:
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100

################################################################################

## Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

## level order traversal
############################
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
    def process_child(self, child_node, prev, leftmost):
        if not child_node:
            return prev, leftmost
        
        if prev:
            prev.next = child_node
        else:
            leftmost = child_node
            
        prev = child_node
        return prev, leftmost
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            
            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)
                curr = curr.next
               
        return root 


class Solution:
    def process_child(self, child_node, prev, leftmost):
        if child_node:
            if prev:
                prev.next = child_node
            else:
                leftmost = child_node
            prev = child_node
            
        return prev, leftmost
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            
            while curr:
                prev, leftmost = self.process_child(curr.left, prev, leftmost)
                prev, leftmost = self.process_child(curr.right, prev, leftmost)
                curr = curr.next
                
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        tail = dummy = Node(0)
        
        node = root
        while node:
            tail.next = node.left
            if tail.next:
                tail = tail.next
                
            tail.next = node.right
            if tail.next:
                tail = tail.next
                
            node = node.next
            if not node:
                tail = dummy
                node = dummy.next
                
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pre_child = child = Node(None)
        curr = root
        while curr:
            while curr:
                child.next = curr.left
                child = child.next or child
                
                child.next = curr.right
                child = child.next or child
                
                curr = curr.next
            curr, child = pre_child.next, pre_child
        
        return root


## Tests
############


## Approach 1: Level Order Traversal
########################################
# Time: O(N)
# Since we process each node exactly once. Note that processing a node in this
# context means popping the node from the queue and then establishing the next
# pointers.

# Space: O(N)
# This is a perfect binary tree which means the last level contains N/2 nodes.
# The space complexity for breadth first traversal is the maximum space occupied# and the space occupied by the queue is dependent upon the maximum number of
# nodes in particular level. So, in this case, the space complexity would be
# O(N).
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
# Space: O(1) - since we don't make use of any additional data structure for
#               traversing nodes on a particular level like the previous
#               approach does.
class Solution:
    
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            
            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = childNode
            else:    
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            prev = childNode 
        return prev, leftmost
    
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        
        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost
            
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None
            
            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                
                # Move onto the next node.
                curr = curr.next
                
        return root

