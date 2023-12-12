##
#### 110. Balanced Binary Tree (easy)
##########################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## top-down recursion
##############################
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        check_height = abs(self.height(root.left) - self.height(root.right)) < 2
        check_left = self.isBalanced(root.left)
        check_right = self.isBalanced(root.right)
        
        return check_height and check_left and check_right
    
    def height(self, root):
        if not root:
            return -1
        
        return 1 + max(self.height(root.left), self.height(root.right))


## bottom-up recursion
##############################
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return True, -1
            
            left_balanced, left_height = helper(node.left)
            
            if not left_balanced:
                return False, 0
            
            right_balanced, right_height = helper(node.right)
            
            if not right_balanced:
                return False, 0
            
            check_height = abs(left_height - right_height) < 2
            height = 1 + max(left_height, right_height)
            
            return check_height, height
        
        return helper(root)[0]


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return True, -1
            
            left_balanced, left_height = helper(node.left)
            right_balanced, right_height = helper(node.right)
            
            if not left_balanced:
                return False, 0
            if not right_balanced:
                return False, 0
            
            check_height = abs(left_height - right_height) < 2
            max_height = 1 + max(left_height, right_height)
            
            return check_height, max_height
        
        return helper(root)[0]


## 
##############################
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
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

