##
#### N-ary Tree Level Order Traversal (medium)
##################################################

# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
 
# Constraints:
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 104]

################################################################################

## Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

## first attempt
##############################
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        res = []
        if not root:
            return res
        
        queue = deque([root])
        while queue:
            res.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                res[-1].append(node.val)
            
                for child in node.children:
                    queue.append(child)
                
        return res


## bfs w/ queue
##############################
class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        res = []
        if not root:
            return res
        
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            res.append(level)
                
        return res


## simplified bfs
##############################
class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        res = []
        if not root:
            return res
        
        prev_level = [root]
        
        while prev_level:
            curr_level = []
            res.append([])
            for node in prev_level:
                res[-1].append(node.val)
                curr_level.extend(node.children)
            prev_level = curr_level
            
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        res = []
        if not root:
            return res
        
        prev_layer = [root]
        
        while prev_layer:
            curr_layer = []
            res.append([])
            for node in prev_layer:
                res[-1].append(node.val)
                curr_layer.extend(node.children)
            prev_layer = curr_layer
                
        return res


## recursive
##############################
class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        res = []
        if not root:
            return res
        
        def traverse_node(node, level):
            if len(res) == level:
                res.append([])
            
            res[level].append(node.val)

            for child in node.children:
                traverse_node(child, level + 1)
                
        traverse_node(root, 0)
        return res


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        def traverse_node(node, level):
            if len(res) == level:
                res.append([])
            
            res[level].append(node.val)

            for child in node.children:
                traverse_node(child, level + 1)
                
        res = []
        
        if root:
            traverse_node(root, 0)
        
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        #self.assertEqual(solution.levelOrder([1,None,3,2,4,None,5,6]), [[1],[3,2,4],[5,6]])
        #self.assertEqual(solution.levelOrder([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]), [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Breadth-first Search using a Queue
######################################################
# Time: O(n)
# - Each node is getting added to the queue, removed from the queue, and added
#   to the result exactly once.

# Space: O(n)
# - We are using a queue to keep track of nodes we still need to visit the
#   children of. At most, the queue will have 2 layers of the tree on it at any
#   given time. In the worst case, this is all of the nodes. In the best case,
#   it is just 1 node (if we have a tree that is equivalent to a linked list).
#   The average case is difficult to calculate without knowing something of the
#   trees we can expect to see, but in balanced trees, half or more of the nodes
#   are often in the lowest 2 layers. So we should go with the worst case of
#   O(n), and know that the average case is probably similar.

def levelOrder(self, root: 'Node') -> List[List[int]]:
    if root is None:
        return []
    result = []
    queue = collections.deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            queue.extend(node.children)
        result.append(level)
    return result


## Approach 2: Simplified Breadth-first Search
##################################################
# Time: O(n) - Where n is the number of nodes.
# Space: O(n) - Same as above, we always have lists containing levels of nodes.
def levelOrder(self, root: 'Node') -> List[List[int]]:
    if root is None:
        return []        

    result = []
    previous_layer = [root]

    while previous_layer:
        current_layer = []
        result.append([])
        for node in previous_layer:
            result[-1].append(node.val)
            current_layer.extend(node.children)
        previous_layer = current_layer
    return result


## Approach 3: Recursion
##############################
# Time: O(n) - Where n is the number of nodes.
# Space: O(log(n)) average case, O(n) worst case - The space used in on the
#                                                  runtime stack.
def levelOrder(self, root: 'Node') -> List[List[int]]:

    def traverse_node(node, level):
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        for child in node.children:
            traverse_node(child, level + 1)

    result = []

    if root is not None:
        traverse_node(root, 0)
    return result


