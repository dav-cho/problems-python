##
#### 133. Clone Graph (medium)
##################################


## Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


## dfs
##############################
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        def dfs(node):
            if not node:
                return
            if node in seen:
                return seen[node]

            clone = Node(node.val)
            seen[node] = clone

            clone.neighbors = [dfs(neighbor) for neighbor in node.neighbors]

            return clone

        seen = {}
        return dfs(node)


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        def dfs(node):
            if not node:
                return
            if node in seen:
                return seen[node]

            clone = Node(node.val)
            seen[node] = clone

            if node.neighbors:
                clone.neighbors = [dfs(neighbor) for neighbor in node.neighbors]

            return clone

        seen = {}

        return dfs(node)


from collections import deque


class Solution:
    def __init__(self):
        self.seen = {}

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return
        if node in self.seen:
            return self.seen[node]

        cloned_node = Node(node.val)
        self.seen[node] = cloned_node

        if node.neighbors:
            cloned_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return cloned_node


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        seen = {}

        def helper(node):
            if not node:
                return
            if node in seen:
                return seen[node]

            cloned = Node(node.val)
            seen[node] = cloned

            if node.neighbors:
                cloned.neighbors = [helper(n) for n in node.neighbors]

            return cloned

        return helper(node)


## dfs
##############################
class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return

        seen = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                seen[curr_node].neighbors.append(seen[neighbor])

        return seen[node]
