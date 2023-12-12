##
#### 429. N-ary Tree Level Order Traversal (medium)
#######################################################


## Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


## first attempt
##############################
from collections import deque


class Solution:
    def levelOrder(self, root: "Node") -> list[list[int]]:
        res = []
        if not root:
            return res

        queue = deque([root])
        while queue:
            res.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                res[-1].append(node.val)

                for child in node.children:
                    queue.append(child)

        return res


## bfs w/ queue
##############################
class Solution:
    def levelOrder(self, root: "Node") -> list[list[int]]:
        res = []
        if not root:
            return res

        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            res.append(level)

        return res


## simplified bfs
##############################
class Solution:
    def levelOrder(self, root: "Node") -> list[list[int]]:
        res = []
        if not root:
            return res

        prev_level = [root]

        while prev_level:
            curr_level = []
            res.append([])
            for node in prev_level:
                res[-1].append(node.val)
                curr_level.extend(node.children)
            prev_level = curr_level

        return res


class Solution:
    def levelOrder(self, root: "Node") -> list[list[int]]:
        res = []
        if not root:
            return res

        prev_layer = [root]

        while prev_layer:
            curr_layer = []
            res.append([])
            for node in prev_layer:
                res[-1].append(node.val)
                curr_layer.extend(node.children)
            prev_layer = curr_layer

        return res


## recursive
##############################
class Solution:
    def levelOrder(self, root: "Node") -> list[list[int]]:
        res = []
        if not root:
            return res

        def traverse_node(node, level):
            if len(res) == level:
                res.append([])

            res[level].append(node.val)

            for child in node.children:
                traverse_node(child, level + 1)

        traverse_node(root, 0)
        return res


class Solution:
    def levelOrder(self, root: "Node") -> list[list[int]]:
        def traverse_node(node, level):
            if len(res) == level:
                res.append([])

            res[level].append(node.val)

            for child in node.children:
                traverse_node(child, level + 1)

        res = []

        if root:
            traverse_node(root, 0)

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        # self.assertEqual(solution.levelOrder([1,None,3,2,4,None,5,6]), [[1],[3,2,4],[5,6]])
        # self.assertEqual(solution.levelOrder([1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]), [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]])


if __name__ == "__main__":
    unittest.main()
