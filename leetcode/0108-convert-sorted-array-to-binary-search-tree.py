##
#### 108. Convert Sorted Array to Binary Search Tree (easy)
###############################################################


## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
## dfs preorder - choose left mid as root - recursive
#########################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def dfs_preorder(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = dfs_preorder(left, mid - 1)
            root.right = dfs_preorder(mid + 1, right)
            
            return root
        
        return dfs_preorder(0, len(nums) - 1)


## dfs preorder - choose left mid as root - iterative
#########################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        root = TreeNode(nums[right // 2])
        stack = [(root, left, right)]
        
        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2
            
            if left < mid:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left, mid - 1))
            if right > mid:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid + 1, right))
                
        return root


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        root = TreeNode(nums[right // 2])
        stack = [(root, left, right)]
        
        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2
            
            if left > right:
                continue
            
            if left < mid:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left, mid - 1))
            if right > mid:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid + 1, right))
                
        return root


## dfs preorder - choose right mid as root - recursive
##########################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def dfs_preorder(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            
            if (left + right) % 2:
                mid += 1
                
            root = TreeNode(nums[mid])
            root.left = dfs_preorder(left, mid - 1)
            root.right = dfs_preorder(mid + 1, right)
            
            return root
        
        return dfs_preorder(0, len(nums) - 1)


## dfs preorder - choose right mid as root - iterative
##########################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
        mid = right // 2
        
        if right % 2:
            mid += 1
            
        root = TreeNode(nums[mid])
        stack = [(root, left, right)]
        
        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2
            
            if (left + right) % 2:
                mid += 1
            
            if left < mid:
                left_mid = (left + mid - 1) // 2
                
                if (left + mid - 1) % 2:
                    left_mid += 1
                    
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left, mid - 1))
            if right > mid:
                right_mid = (mid + 1 + right) // 2
                
                if (mid + 1 + right) % 2:
                    right_mid += 1
                
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid + 1, right))
                
        return root


## dfs preorder - choose random mid node as root - recursive
################################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def dfs_preorder(left, right):
            if left > right:
                return
            
            mid = (left + right) // 2
            
            if (left + right) % 2:
                mid += randint(0, 1)
                
            root = TreeNode(nums[mid])
            root.left = dfs_preorder(left, mid - 1)
            root.right = dfs_preorder(mid + 1, right)
            
            return root
        
        return dfs_preorder(0, len(nums) - 1)


## dfs preorder - choose random mid node as root - iterative
################################################################
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()

