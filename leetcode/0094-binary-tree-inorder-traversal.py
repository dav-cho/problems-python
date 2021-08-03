##
#### Binary Tree Inorder Traversal (easy)
#############################################

# Given the root of a binary tree, return the inorder traversal of its
# nodes' values.

# Example 1:
#       1
#         2
#       3
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
#       1
#     2
# Input: root = [1,2]
# Output: [2,1]

# Example 5:
#       1
#         2
# Input: root = [1,null,2]
# Output: [1,2]
 
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 
# Follow up: Recursive solution is trivial, could you do it iteratively?

################################################################################

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## recursive
################
class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        result = []
        self.helper(root, result)
        return result
    
    def helper(self, node, result):
        if not node:
            return
        
        self.helper(node.left, result)
        result.append(node.val)
        self.helper(node.right, result)


## iterative
################
class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        result, stack = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            root = stack.pop()
            result.append(root.val)
            root = root.right
            
        return result


## morris traversal
#######################
class Solution:
    def inorder_traversal(self, root: TreeNode) -> list[int]:
        result = []
        while root:
            if not root.left:
                result.append(root.val)
                root = root.right
            else:
                pred = root.left
                
                while pred.right:
                    pred = pred.right
                    
                pred.right = root
                root.left, root = None, root.left
                
        return result


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Recursive Approach
#####################################
# time: O(n) - The time complexity is O(n) because the recursive function is
#              T(n) = 2 * T(n / 2) + 1.
# space: O(n) - The worst case space required is O(n), and in the average case
#               it's O(log(n)) where n is number of nodes.

## Java
#class Solution {
#    public List < Integer > inorderTraversal(TreeNode root) {
#        List < Integer > res = new ArrayList < > ();
#        helper(root, res);
#        return res;
#    }
#
#    public void helper(TreeNode root, List < Integer > res) {
#        if (root != null) {
#            if (root.left != null) {
#                helper(root.left, res);
#            }
#            res.add(root.val);
#            if (root.right != null) {
#                helper(root.right, res);
#            }
#        }
#    }
#}


## Approach 2: Iterating method using Stack
###############################################
# time: O(n)
# space: O(n)

## Java
#public class Solution {
#    public List < Integer > inorderTraversal(TreeNode root) {
#        List < Integer > res = new ArrayList < > ();
#        Stack < TreeNode > stack = new Stack < > ();
#        TreeNode curr = root;
#        while (curr != null || !stack.isEmpty()) {
#            while (curr != null) {
#                stack.push(curr);
#                curr = curr.left;
#            }
#            curr = stack.pop();
#            res.add(curr.val);
#            curr = curr.right;
#        }
#        return res;
#    }
#}

## Approach 3: Morris Traversal
###################################
# time: O(n) - To prove that the time complexity is O(n), the biggest problem
#              lies in finding the time complexity of finding the predecessor
#              nodes of all the nodes in the binary tree. Intuitively, the
#              complexity is O(n log(n)), because to find the predecessor node
#              for a single node related to the height of the tree. But in fact,
#              finding the predecessor nodes for all nodes only needs O(n) time.
#              Because a binary Tree with nn nodes has n − 1 edges, the whole
#              processing for each edges up to 2 times, one is to locate a node,
#              and the other is to find the predecessor node. So the complexity
#              is O(n).
# space: O(n) - Arraylist of size n is used.

## Java
#class Solution {
#    public List < Integer > inorderTraversal(TreeNode root) {
#        List < Integer > res = new ArrayList < > ();
#        TreeNode curr = root;
#        TreeNode pre;
#        while (curr != null) {
#            if (curr.left == null) {
#                res.add(curr.val);
#                curr = curr.right; // move to next right node
#            } else { // has a left subtree
#                pre = curr.left;
#                while (pre.right != null) { // find rightmost
#                    pre = pre.right;
#                }
#                pre.right = curr; // put cur after the pre node
#                TreeNode temp = curr; // store cur node
#                curr = curr.left; // move cur to the top of the new tree
#                temp.left = null; // original cur left be null, avoid infinite loops
#            }
#        }
#        return res;
#    }
#}

