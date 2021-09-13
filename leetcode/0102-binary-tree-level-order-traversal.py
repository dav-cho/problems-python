##
#### Binary Tree Level Order Traversal (medium)
###################################################

# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

################################################################################

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
################
class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        def bfs(node, level):
            if len(res) == level:
                res.append([])
                
            res[level].append(node.val)
            
            if node.left:
                bfs(node.left, level + 1)
            if node.right:
                bfs(node.right, level + 1)
                
        bfs(root, 0)
        return res


class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        def helper(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        
        helper(root, 0)
        return result


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if not root:
            return result
        
        self.helper(root, 0, result)
        return result
    
    def helper(self, node, level, result):
        if len(result) == level:
            result.append([])

        result[level].append(node.val)

        if node.left:
            self.helper(node.left, level + 1, result)
        if node.right:
            self.helper(node.right, level + 1, result)


## iterative
################
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        level = 0
        queue = deque([root])
        while queue:
            result.append([])
            
            for _ in range(len(queue)):
                node = queue.popleft()
                result[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level += 1
            
        return result


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        level = 0
        queue = deque([root])
        while queue:
            result.append([])
            len_level = len(queue)
            
            for _ in range(len_level):
                node = queue.popleft()
                result[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level += 1
            
        return result


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Recursion
############################
# time: O(N) - since each node is processed exactly once.
# space: O(N) - to keep the output structure which contains N node values.
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels


## Approach 2: Iteration
############################
# time: O(N) - since each node is processed exactly once.
# space: O(N) - to keep the output structure which contains N node values.
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels


