##
#### 102. Binary Tree Level Order Traversal (medium)
########################################################



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
