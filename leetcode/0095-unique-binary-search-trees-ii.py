##
#### Unique Binary Search Trees II (medium)
###############################################

# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.

# Example 1:
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

# Example 2:
# Input: n = 1
# Output: [[1]]
  
# Constraints:
# 1 <= n <= 8

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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate_trees(start, i - 1)
                right_trees = generate_trees(i + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        curr_tree = TreeNode(i)
                        curr_tree.left = l
                        curr_tree.right = r
                        all_trees.append(curr_tree)
                        
            return all_trees
        
        return generate_trees(1, n) if n else []


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start, end):
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                left = generate(start, i - 1)
                right = generate(i + 1, end)
                
                for l in left:
                    for r in right:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        all_trees.append(curr)
                        
            return all_trees
        
        return generate(1, n) if n else []


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Recursion
##############################
# Time: O(4^n / (n^(1/2)))
# The main computations are to construct all possible trees with a given root,
# that is actually Catalan number G(sub)n as was discussed above. This is done
# n times, that results in time complexity nG(sub. Catalan numbers grow as
# 4^n / n^(3/2) that gives the final complexity O(4^n / (n^(1/2)). Seems to be
# large but let's not forget that here we're asked to generate
# G(sub)n ∼ 4^n / (n&(3/2) tree objects as output.

# Space: O(4^n / (n^(1/2)))
# nG(sub)n as we keep G(sub)n trees with n elements each.

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)
                
                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)
                
                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            
            return all_trees
        
        return generate_trees(1, n) if n else []


