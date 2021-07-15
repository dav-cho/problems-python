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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## Approach 1: Recursion
############################
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        pass


## Approach 2: Tail Recursion + BFS
#######################################
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        pass


## Approach 3: Iteration
############################
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        pass


## Approach 1: Recursion
############################
# time: O(n)
# space: O(log(n))
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
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
# time: O(n)
# space: O(2^log(n - 1)) = O(n/2) = O(n)
# tail recursion can optimize stack overhead in languages like C++
# not supported by python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        pass


# C++
# class Solution {
#
#   private:
#     // The queue that contains the next nodes to visit,
#     //   along with the level/depth that each node is located.
#     queue<pair<TreeNode*, int>> next_items;
#     int max_depth = 0;
#
#     /**
#      * A tail recursion function to calculate the max depth
#      *   of the binary tree.
#      */
#     int next_maxDepth() {
#
#       if (next_items.size() == 0) {
#         return max_depth;
#       }
#
#       auto next_item = next_items.front();
#       next_items.pop();
#
#       auto next_node = next_item.first;
#       auto next_level = next_item.second + 1;
#
#       max_depth = max(max_depth, next_level);
#
#       // Add the nodes to visit in the following recursive calls.
#       if (next_node->left != NULL) {
#         next_items.push(make_pair(next_node->left, next_level));
#       }
#       if (next_node->right != NULL) {
#         next_items.push(make_pair(next_node->right, next_level));
#       }
#
#       // The last action should be the ONLY recursive call
#       //   in the tail-recursion function.
#       return next_maxDepth();
#     }
#
#   public:
#     int maxDepth(TreeNode* root) {
#       if (root == NULL) return 0;
#
#       // clear the previous queue.
#       std::queue<pair<TreeNode*, int>> empty;
#       std::swap(next_items, empty);
#       max_depth = 0;
#
#       // push the root node into the queue to kick off the next visit.
#       next_items.push(make_pair(root, 0));
#
#       return next_maxDepth();
#     }
# };

## Approach 3: Iteration
############################
# time: O(n)
# space: O(log(n))
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


def test(*args):
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = maxDepth(test)
            print(f"test: {count}")
            print(f"result {count}: {result}")

    return run()


test1 = [3, 9, 20, None, None, 15, 7]  # 3
test2 = [1, None, 2]  # 2
test3 = []  # 0
test4 = [0]  # 1

test(test1, test2, test3, test4)
