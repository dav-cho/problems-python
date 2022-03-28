##
#### 286. Walls and Gates (medium)
######################################


## brute force
##################
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """


## bfs
##################
class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        if not rooms:
            return

        rows = len(rooms)
        cols = len(rooms[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        empty = 2**31 - 1

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            for x, y in directions:
                r = row + x
                c = col + y
                if r < 0 or r >= rows:
                    continue
                if c < 0 or c >= cols:
                    continue
                if rooms[r][c] != empty:
                    continue

                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))
