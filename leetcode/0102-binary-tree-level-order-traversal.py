##
#### Binary Tree Level Order Traversal (medium)
###################################################

# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).

# Example 1:
#      3
#   9    20
#      15  7
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
##############################
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def bfs(node, level):
            if not node:
                return
            if len(res) == level:
                res.append([])
                
            res[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
            
            return res
        
        return bfs(root, 0)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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


## iterative
##############################
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = deque([root])
        level = 0
        while queue:
            res.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
            
        return res


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        queue = [root]
        level = 0
        while queue:
            res.append([])
            next_queue = []
            for node in queue:
                res[level].append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            level += 1
            
        return res


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [root]
        level = 0
        while queue:
            res.append([])
            next_queue = []
            for node in queue:
                if not node:
                    return []
                res[level].append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            level += 1
            
        return res


## 
##############################
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


## 
##############################
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


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


## LeetCode Solutions
#########################

## Approach 1: Recursion
##############################
# Time: O(N) - Since each node is processed exactly once.
# Space: O(N) - To keep the output structure which contains N node values.
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
##############################
# Time: O(N) - Since each node is processed exactly once.
# Space: O(N) - To keep the output structure which contains N node values.
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


