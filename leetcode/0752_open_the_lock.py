##
#### 752. Open the Lock (medium)
####################################


## bfs
##########
from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def neighbors(node):
            # for wheel in range(len(node):
            for wheel in range(4):
                digit = int(node[wheel])
                for turn in (-1, 1):
                    digit_neighbor = (digit + turn) % 10
                    yield node[:wheel] + str(digit_neighbor) + node[wheel + 1 :]

        dead = set(deadends)
        seen = {"0000"}
        queue = deque([("0000", 0)])
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in dead:
                continue

            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return -1
