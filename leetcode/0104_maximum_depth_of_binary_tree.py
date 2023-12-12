##
#### 104. Maximum Depthof Binary Tree (easy)
################################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
##############################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(map(self.maxDepth, (root.left, root.right))) + 1 if root else 0


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node, depth):
            if not node:
                return 0
            
            self.res = max(self.res, depth)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
            return self.res
            
        return dfs(root, 1)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(node, depth):
            nonlocal res
            if not node:
                return 0
            
            res = max(res, depth)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
            return res
            
        return dfs(root, 1)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node, depth):
            if not node:
                return 0
            
            self.res = max(self.res, depth)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root, 1)
        return self.res


## tail recursion + bfs
##############################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(node, level):
            if not node:
                return 0
                
            self.res = max(self.res, level)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
            
            return self.res
        
        self.res = 0
        return bfs(root, 1)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def bfs():
            nonlocal depth
                
            while queue:
                node, level = queue.popleft()

                depth = max(depth, level)

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

            return depth
        
        queue = deque([(root, 1)])
        depth = 0
        
        return bfs()


## iterative
##############################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        depth = 0
        
        if root:
            stack.append((root, 1))
            
        while stack:
            root, curr_depth = stack.pop()
            
            if root:
                depth = max(depth, curr_depth)
                stack.append((root.left, curr_depth + 1))
                stack.append((root.right, curr_depth + 1))
                
        return depth


## iterative bfs
##############################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        
        queue = [root]
        while queue:
            res += 1
            level = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            queue = level
                    
        return res


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                
        return depth


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [root]
        depth = 0
        
        while queue:
            depth += 1
            level = []
            
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                    
            queue = level
            
        return depth


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()

