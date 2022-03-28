##
#### 236. Lowest Common Ancestor of a Binary Tree (medium)
##############################################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


## recursive
##############################
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node == p or node == q
            if mid + left + right >= 2:
                self.res = node
                
            return left or right or mid
        
        dfs(root)
        return self.res


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None;
        
        def dfs(node):
            nonlocal res
            
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node == p or node == q
            if left + right + mid >= 2:
                res = node
                
            return left or right or mid
        
        dfs(root)
        return res


## iterative w/ parent pointers
###################################
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parents = {root: None}
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
                
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        while q not in ancestors:
            q = parents[q]
            
        return q


## iterative w/o parent pointers
####################################
class Solution:
    BOTH_PENDING = 2
    LEFT_DONE = 1
    BOTH_DONE = 0
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [(root, Solution.BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != Solution.BOTH_DONE:
                if parent_state == Solution.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None                


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.BOTH_PENDING = 2
        self.LEFT_PENDING = 1
        self.BOTH_DONE = 0
    
        stack = [(root, self.BOTH_PENDING)]
        one_node_found = False
        lca_idx = -1
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != self.BOTH_DONE:
                if parent_state == self.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[lca_idx][0]
                        else:
                            one_node_found = True
                            lca_idx = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append((child_node, self.BOTH_PENDING))
            else:
                if one_node_found and lca_idx == len(stack) - 1:
                    lca_idx -= 1
                stack.pop()
                
        return None


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
