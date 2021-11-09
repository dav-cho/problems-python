##
#### Maximum Depthof Binary Tree (easy)
###########################################

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Example 3:
# Input: root = []
# Output: 0

# Example 4:
# Input: root = [0]
# Output: 1
 
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            
        return max(left, right) + 1


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(map(self.maxDepth, (root.left, root.right))) + 1 if root else 0


## tail recursion + bfs
##############################
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


## bfs
##############################
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


## LeetCode Solutions
#########################

## Approach 1: Recursion
##############################
# Time: O(N)
# - We visit each node exactly once, thus the time complexity is O(N), where N
#   is the number of nodes.

# Space: O(N)
# - In the worst case, the tree is completely unbalanced, e.g. each node has
#   only left child node, the recursion call would occur N times (the height of
#   the tree), therefore the storage to keep the call stack would be O(N). But
#   in the best case (the tree is completely balanced), the height of the tree
#   would be log(N). Therefore, the space complexity in this case would
#   be O(log(N)).
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1


## Approach 2: Tail Recursion + BFS
#######################################
# Time: O(N) - Still we visit each node and only once.
# Space: O(N) - The maximun number of nodes at the same level (the number of
#               leaf nodes in a full binary tree), since we traverse the tree
#               in the bfs manner.
#               O(2^(log_2(N - 1))) = O(N/2) = O(N)

# - As one can see, this probably is not the best example to apply the tail
#   recursion technique. Because though we did gain the constant space
#   complexity for the recursive calls, we pay the price of O(N) complexity to
#   maintain the state information for recursive calls. This defeats the
#   purpose of applying tail recursion.
# - However, we would like to stress on the point that tail recursion is a
#   useful form of recursion that could eliminate the space overhead incurred
#   by the recursive function calls.

# Note: a function cannot be tail recursion if there are multiple occurrences of
# recursive calls in the function, even if the last action is the recursive
# call. Because the system has to maintain the function call stack for the
# sub-function calls that occur within the same function.

## C++
#class Solution {
#
#  private:
#    // The queue that contains the next nodes to visit, 
#    //   along with the level/depth that each node is located.
#    queue<pair<TreeNode*, int>> next_items;
#    int max_depth = 0;
#    
#    /**
#     * A tail recursion function to calculate the max depth
#     *   of the binary tree.
#     */
#    int next_maxDepth() {
#    
#      if (next_items.size() == 0) {
#        return max_depth;
#      }
#        
#      auto next_item = next_items.front();
#      next_items.pop();
#
#      auto next_node = next_item.first;
#      auto next_level = next_item.second + 1;
#      
#      max_depth = max(max_depth, next_level);
#
#      // Add the nodes to visit in the following recursive calls.
#      if (next_node->left != NULL) {
#        next_items.push(make_pair(next_node->left, next_level));
#      }
#      if (next_node->right != NULL) {
#        next_items.push(make_pair(next_node->right, next_level));
#      }
#    
#      // The last action should be the ONLY recursive call
#      //   in the tail-recursion function.
#      return next_maxDepth();
#    }
#    
#  public:
#    int maxDepth(TreeNode* root) {
#      if (root == NULL) return 0;
#        
#      // clear the previous queue.
#      std::queue<pair<TreeNode*, int>> empty;
#      std::swap(next_items, empty);
#      max_depth = 0;
#        
#      // push the root node into the queue to kick off the next visit.
#      next_items.push(make_pair(root, 0));
#        
#      return next_maxDepth();
#    }
#};


## Approach 3: Iteration
##############################
# Time: O(N)
# Space: O(logN)
# - In the worst case, the tree is completely unbalanced, e.g. each node has
#   only left child node, the recursion call would occur N times (the height of
#   the tree), therefore the storage to keep the call stack would be O(N). But
#   in the average case (the tree is balanced), the height of the tree would be
#   log(N). Therefore, the space complexity in this case would be O(log(N)).

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth


