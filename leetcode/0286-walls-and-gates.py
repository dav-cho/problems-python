##
#### Walls and Gates (medium)
#################################

# You are given an m x n grid rooms initialized with these three possible
# values.

# - -1 A wall or an obstacle.
# - 0 A gate.
# - INF Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to
#   represent INF as you may assume that the distance to a gate is less than
#   2147483647.
# - Fill each empty room with the distance to its nearest gate. If it is
#   impossible to reach a gate, it should be filled with INF.

# Example 1:
# Input: rooms = [[2147483647,-1,0,2147483647],
#                [2147483647,2147483647,2147483647,-1],
#                [2147483647,-1,2147483647,-1],
#                [0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Example 2:
# Input: rooms = [[-1]]
# Output: [[-1]]

# Example 3:
# Input: rooms = [[2147483647]]
# Output: [[2147483647]]

# Example 4:
# Input: rooms = [[0]]
# Output: [[0]]
 
# Constraints:
# m == rooms.length
# n == rooms[i].length
# 1 <= m, n <= 250
# rooms[i][j] is -1, 0, or 2^31 - 1.

################################################################################

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
        empty = 2 ** 31 - 1
        
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


## Tests
#############


## LeetCode Solutions
#########################

## Approach 1: (Brute Force) [Time Limit Exceeded]
######################################################
# Time: O(m^2 n^2) - For each point in the m \times nm×n size grid, the gate
#                    could be at most m \times nm×n steps away.
# Space: O(mn) - The space complexity depends on the queue's size. Since
#                we won't insert points that have been visited before into the
#                queue, we insert at most m \times nm×n points into the queue.
## Java
#private static final int EMPTY = Integer.MAX_VALUE;
#private static final int GATE = 0;
#private static final int WALL = -1;
#private static final List<int[]> DIRECTIONS = Arrays.asList(
#        new int[] { 1,  0},
#        new int[] {-1,  0},
#        new int[] { 0,  1},
#        new int[] { 0, -1}
#);
#
#public void wallsAndGates(int[][] rooms) {
#    if (rooms.length == 0) return;
#    for (int row = 0; row < rooms.length; row++) {
#        for (int col = 0; col < rooms[0].length; col++) {
#            if (rooms[row][col] == EMPTY) {
#                rooms[row][col] = distanceToNearestGate(rooms, row, col);
#            }
#        }
#    }
#}
#
#private int distanceToNearestGate(int[][] rooms, int startRow, int startCol) {
#    int m = rooms.length;
#    int n = rooms[0].length;
#    int[][] distance = new int[m][n];
#    Queue<int[]> q = new LinkedList<>();
#    q.add(new int[] { startRow, startCol });
#    while (!q.isEmpty()) {
#        int[] point = q.poll();
#        int row = point[0];
#        int col = point[1];
#        for (int[] direction : DIRECTIONS) {
#            int r = row + direction[0];
#            int c = col + direction[1];
#            if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] == WALL
#                    || distance[r][c] != 0) {
#                continue;
#            }
#            distance[r][c] = distance[row][col] + 1;
#            if (rooms[r][c] == GATE) {
#                return distance[r][c];
#            }
#            q.add(new int[] { r, c });
#        }
#    }
#    return Integer.MAX_VALUE;
#}


## Approach 2: (Breadth-first Search) [Accepted]
####################################################
# Time: O(mn)
# - If you are having difficulty to derive the time complexity, start simple.
# - Let us start with the case with only one gate. The breadth-first search
#   takes at most m \times nm×n steps to reach all rooms, therefore the time
#   complexity is O(mn). But what if you are doing breadth-first search from
#   k gates?
# - Once we set a room's distance, we are basically marking it as visited,
#   which means each room is visited at most once. Therefore, the time
#   complexity does not depend on the number of gates and is O(mn).

# Space: O(mn) - The space complexity depends on the queue's size. We insert
#                at most m * n points into the queue.

# I think what some folks are missing in this second solution is that each gate
# is not fully searched before moving on to a new gate. Each gate only looks at
# the areas within 1 space before we check the next gate. So each area within
# one space of the gates are checked for rooms and these rooms are marked, then
# added to the queue. Once all gates are checked, each new space is checked,
# and so forth. So, once a room gets hit, it has to be from the closest gate.

## Java
#private static final int EMPTY = Integer.MAX_VALUE;
#private static final int GATE = 0;
#private static final List<int[]> DIRECTIONS = Arrays.asList(
#        new int[] { 1,  0},
#        new int[] {-1,  0},
#        new int[] { 0,  1},
#        new int[] { 0, -1}
#);
#
#public void wallsAndGates(int[][] rooms) {
#    int m = rooms.length;
#    if (m == 0) return;
#    int n = rooms[0].length;
#    Queue<int[]> q = new LinkedList<>();
#    for (int row = 0; row < m; row++) {
#        for (int col = 0; col < n; col++) {
#            if (rooms[row][col] == GATE) {
#                q.add(new int[] { row, col });
#            }
#        }
#    }
#    while (!q.isEmpty()) {
#        int[] point = q.poll();
#        int row = point[0];
#        int col = point[1];
#        for (int[] direction : DIRECTIONS) {
#            int r = row + direction[0];
#            int c = col + direction[1];
#            if (r < 0 || c < 0 || r >= m || c >= n || rooms[r][c] != EMPTY) {
#                continue;
#            }
#            rooms[r][c] = rooms[row][col] + 1;
#            q.add(new int[] { r, c });
#        }
#    }
#}


## Discuss Solutions
########################
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
        for i, j in q:
            for I, J in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2 ** 30:
                    rooms[I][J] = rooms[i][j] + 1
                    q += (I, J),


from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        
        rows = len(rooms)
        cols = len(rooms[0])
        
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    queue = deque()
                    queue.append((i + 1, j, 1))
                    queue.append((i - 1, j, 1))
                    queue.append((i, j + 1, 1))
                    queue.append((i, j - 1, 1))
                    
                    seen = set()
                    while queue:
                        row, col, val = queue.popleft()
                        
                        if row < 0 or row = rows or col < 0 or col >= cols or rooms[row][col] in [0, -1] or (row, col) in seen:
                            continue
                            
                        seen.add((row, col))
                        rooms[row][col] = min(rooms[row][col], val)
                        
                        queue.append((row + 1, col, val + 1))
                        queue.append((row - 1, col, val + 1))
                        queue.append((row, col + 1, val + 1))
                        queue.append((row, col - 1, val + 1))>


## TODO
##############
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        queue = deque()
        rows = len(rooms)
        cols = len(rooms[0])
        
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col, 0))
                    
        while queue:
            row, col, dist = queue.popleft()
            
            if row > 0 and rooms[row - 1][col] == 2147483647:
                rooms[row - 1][col] = dist + 1
                queue.append((row - 1, col, dist + 1))
            if row < rows - 1 and rooms[row + 1][col] == 2147483647:
                rooms[row + 1][col] = dist + 1
                queue.append(row + 1, col, dist + 1))
            if col > 0 and rooms[row][col - 1] == 2147483647:
                rooms[row][col - 1] = dist + 1
                queue.append((row, col - 1, dist + 1))
            if col < cols and rooms[row][col - 1] == 2147483647:
                rooms[row][col - 1] = dist + 1
                queue.append((row, col + 1, dist + 1))(


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return
        
        rows = len(rooms)
        cols = len(rooms[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    queue.append((row, col))
                    
        while queue:
            row, col = queue.pop()
            for direction in directions:
                x, y = direction
                r = row + x
                c = col + y
                if r < 0 or c < 0 or r >= rows or c >= cols or rooms[r][c]:
                    continue
                
                rooms[r][c] = rooms[row][col] + 1
                queue.append((r, c))


