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


# Approach 1: Recursion
# time: O(n)
# space: O(log(n))
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    right = maxDepth(root.right)
    left = maxDepth(root.left)

    return max(right, left) + 1


# Approach 2: Tail Recursion + BFS
# tail recursion can optimize stack overhead in languages like C++
# not supported by python
def maxDepth(root: TreeNode) -> int:
    pass


# Approach 3: Iteration
# time: O(n)
# space: O(log(n))
def maxDepth(root: TreeNode) -> int:
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
