##
#### Maximum Depth of Binary Tree (easy)
############################################

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the
# longest path from the root node down to the farthest leaf node.

# Example 1:
#         3
#    9         20
#           15    7

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

########################################################################

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## iterative - most optimal
###############################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, curr_depth = stack.pop()
            
            if not node:
                continue
            
            depth = max(depth, curr_depth)
            stack.append((node.left, curr_depth + 1))
            stack.append((node.right, curr_depth + 1))
            
        return depth


## recursion and dfs
########################
class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        
        return max(left, right) + 1


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        def helper(root, depth):
            if not root:
                return depth
            
            left = helper(root.left, depth + 1)
            right = helper(root.right, depth + 1)
            
            return max(left, right)
        
        return helper(root, 0)


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        def helper(root, depth):
            if not root:
                return 0
            if not root.left and not root.right:
                return depth

            left = helper(root.left, depth + 1)
            right = helper(root.right, depth + 1)
            
            return max(left, right)
            
        return helper(root, 1)


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        return self.helper(root, 0)
    
    def helper(self, root, depth):
        if not root:
            return depth

        left = self.helper(root.left, depth + 1)
        right = self.helper(root.right, depth + 1)

        return max(left, right)


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        return self.helper(root, 1)
    
    
    def helper(self, root, depth):
        if not root:
            return 0
        if not root.left and not root.right:
            return depth

        left = self.helper(root.left, depth + 1)
        right = self.helper(root.right, depth + 1)

        return max(left, right)


## tail recursion + bfs
###############################
class Solution:
    def max_depth(self, root: TreeNode) -> int:
        pass


## iterative
################
class Solution:
    def max_depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, 1)]
        depth = 0
        while stack:
            node, curr_depth = stack.pop()
            if not node:
                continue
                
            depth = max(depth, curr_depth)
            stack.append((node.left, curr_depth + 1))
            stack.append((node.right, curr_depth + 1))
            
        return depth


class Solution:
    def max_depth(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append((root, 1))
            
        depth = 0
        while stack:
            root, curr_depth = stack.pop()
            if not root:
                continue
            
            depth = max(depth, curr_depth)
            stack.append((root.left, curr_depth + 1))
            stack.append((root.right, curr_depth + 1))
                
        return depth


## iterative 2
##################
class Solution:
    def max_depth(self, root: TreeNode) -> int:
        stack = []
        if root:
            stack.append((root, 1))
        
        depth = 0
        while stack:
            root, curr_depth = stack.pop()
            if root:
                depth = max(depth, curr_depth)
                stack.append((root.left, curr_depth + 1))
                stack.append((root.right, curr_depth + 1))
                
        return depth


## recursive one line
#########################
class Solution:
    def max_depth(self, root: TreeNode) -> int:
        return 1 + max(map(self.max_depth, (root.left, root.right))) if root else 0


## Tests
############

test1 = [3, 9, 20, None, None, 15, 7]   # 3
test2 = [1, None, 2]                    # 2
test3 = []                              # 0
test4 = [0]                             # 1

tests = (
    test1,
    test2,
    test3,
    test4,
)


def test(*args):
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = max_depth(test)
            print(f"test: {count}")
            print(f"result {count}: {result}")

    return run()


test(*tests)


## Approach 1: Recursion
############################
# time: O(N) - We visit each node exactly once, thus the time complexity is
#              O(N), where N is the number of nodes.
# space: O(N) - In the worst case, the tree is completely unbalanced, e.g. each
#               node has only left child node, the recursion call would occur N
#               times (the height of the tree), therefore the storage to keep
#               the call stack would be O(N). But in the best case (the tree is
#               completely balanced), the height of the tree would be log(N).
#               Therefore, the space complexity in this case would be O(log(N)).
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
# time: O(N) - Still we visit each node once and only once.
# space: O(N) - i.e. the maximum number of nodes at the same level (the number
#               of leaf nodes in a full binary tree), since we traverse the tree#               in the BFS manner. 
#               O(2 ^ (log(N - 1)) == O(N / 2) == O(N)

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
############################
# time: O(N)
# space: O(N) - in the worst case, the tree is completely unbalanced, e.g. each
#               node has only left child node, the recursion call would occur N
#               times (the height of the tree), therefore the storage to keep
#               the call stack would be O(N). But in the average case (the tree
#               is balanced), the height of the tree would be log(N). Therefore,#               the space complexity in this case would be O(log(N)).
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

