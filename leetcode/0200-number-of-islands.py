##
#### Number of Islands (medium)
###################################

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

################################################################################

## dfs
##########
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        result = 0
        if not grid:
            return result
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    result += 1
                    self.dfs(row, col, grid)
        
        return result
        
    def dfs(self, row, col, grid):
        if not 0 <= row < len(grid):
            return
        if not 0 <= col < len(grid[0]):
            return
        if grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in directions:
            self.dfs(row + x, col + y, grid)


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(row, col):
            if not 0 <= row < num_rows:
                return
            if not 0 <= col < num_cols:
                return
            if grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            for direction in directions:
                dfs(row + direction[0], col + direction[1])
                
        result = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    result += 1
                    dfs(row, col)
                    
        return result


## bfs
##########
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        result = 0
        if not grid:
            return result
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != '1':
                    continue
                
                result += 1
                grid[row][col] = '0'
                queue = [(row, col)]
                while queue:
                    curr_row, curr_col = queue.pop()
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for x, y in directions:
                        r = curr_row + x
                        c = curr_col + y
                        if not 0 <= r < num_rows:
                            continue
                        if not 0 <= c < num_cols:
                            continue
                        if grid[r][c] != '1':
                            continue
                            
                        grid[r][c] = '0'
                        queue.append((r, c))
                        
        return result


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        result = 0
        if not grid:
            return result
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != '1':
                    continue
                    
                result += 1
                grid[row][col] = '0'
                queue = [(row, col)]
                while queue:
                    r, c = queue.pop()
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for x, y in directions:
                        if not 0 <= r + x < num_rows:
                            continue
                        if not 0 <= c + y < num_cols:
                            continue
                        if grid[r + x][c + y] != '1':
                            continue
                        
                        grid[r + x][c + y] = '0'
                        queue.append(((r + x), (c + y)))
                        
        return result


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        result = 0
        if not grid:
            return result
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != '1':
                    continue
                
                result += 1
                grid[row][col] = '0'
                queue = []
                queue.append(row * num_cols + col)
                
                while queue:
                    idx = queue.pop()
                    r, c = divmod(idx, num_cols)
                    print(r, c)
                    
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for x, y in directions:
                        if not 0 <= r + x < num_rows:
                            continue
                        if not 0 <= c + y < num_cols:
                            continue
                        if grid[r + x][c + y] != '1':
                            continue
                            
                        grid[r + x][c + y] = '0'
                        queue.append((r + x) * num_cols + (c + y))
                        
        return result


## union find
#################
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        pass


## Tests
#############

test1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]   # 1
test2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]   # 3
test3 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]   # 1

tests = [
    test1,      # 1
    test2,      # 3
    test3,       # 1
]

def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            solution = Solution()
            result = solution.numIslands(test)

            print("result:", result)

    return run()


test(*tests)


## LeetCode Solutions
#########################

## Approach 1: DFS [Accepted]
#################################
# Time: O(M * N) - Where M is the number of rows and N is the number of columns.
# Space: O(M * N) - Worst case O(M×N) in case that the grid map is filled with
#                   lands where DFS goes by M×N deep.
## Java
#class Solution {
#  void dfs(char[][] grid, int r, int c) {
#    int nr = grid.length;
#    int nc = grid[0].length;
#
#    if (r < 0 || c < 0 || r >= nr || c >= nc || grid[r][c] == '0') {
#      return;
#    }
#
#    grid[r][c] = '0';
#    dfs(grid, r - 1, c);
#    dfs(grid, r + 1, c);
#    dfs(grid, r, c - 1);
#    dfs(grid, r, c + 1);
#  }
#
#  public int numIslands(char[][] grid) {
#    if (grid == null || grid.length == 0) {
#      return 0;
#    }
#
#    int nr = grid.length;
#    int nc = grid[0].length;
#    int num_islands = 0;
#    for (int r = 0; r < nr; ++r) {
#      for (int c = 0; c < nc; ++c) {
#        if (grid[r][c] == '1') {
#          ++num_islands;
#          dfs(grid, r, c);
#        }
#      }
#    }
#
#    return num_islands;
#  }
#}


## Approach 2: BFS [Accepted]
################################
# Time: O(M * N) - Where M is the number of rows and N is the number of columns.
# Space: O(min(M, N)) - Because in worst case where the grid is filled with
#                       lands, the size of queue can grow up to min(M,N).

## Java
#class Solution {
#  public int numIslands(char[][] grid) {
#    if (grid == null || grid.length == 0) {
#      return 0;
#    }
#
#    int nr = grid.length;
#    int nc = grid[0].length;
#    int num_islands = 0;
#
#    for (int r = 0; r < nr; ++r) {
#      for (int c = 0; c < nc; ++c) {
#        if (grid[r][c] == '1') {
#          ++num_islands;
#          grid[r][c] = '0'; // mark as visited
#          Queue<Integer> neighbors = new LinkedList<>();
#          neighbors.add(r * nc + c);
#          while (!neighbors.isEmpty()) {
#            int id = neighbors.remove();
#            int row = id / nc;
#            int col = id % nc;
#            if (row - 1 >= 0 && grid[row-1][col] == '1') {
#              neighbors.add((row-1) * nc + col);
#              grid[row-1][col] = '0';
#            }
#            if (row + 1 < nr && grid[row+1][col] == '1') {
#              neighbors.add((row+1) * nc + col);
#              grid[row+1][col] = '0';
#            }
#            if (col - 1 >= 0 && grid[row][col-1] == '1') {
#              neighbors.add(row * nc + col-1);
#              grid[row][col-1] = '0';
#            }
#            if (col + 1 < nc && grid[row][col+1] == '1') {
#              neighbors.add(row * nc + col+1);
#              grid[row][col+1] = '0';
#            }
#          }
#        }
#      }
#    }
#
#    return num_islands;
#  }
#}


## Approach 3: Union Find (aka Disjoint Set) [Accepted]
###########################################################
# Time: O(M * N) - Where M is the number of rows and N is the number of columns.
#                  Note that Union operation takes essentially constant time
#                  when UnionFind is implemented with both path compression and
#                  union by rank.
# Space: O(M * N) - As required by UnionFind data structure.

## Java
#class Solution {
#  class UnionFind {
#    int count; // # of connected components
#    int[] parent;
#    int[] rank;
#
#    public UnionFind(char[][] grid) { // for problem 200
#      count = 0;
#      int m = grid.length;
#      int n = grid[0].length;
#      parent = new int[m * n];
#      rank = new int[m * n];
#      for (int i = 0; i < m; ++i) {
#        for (int j = 0; j < n; ++j) {
#          if (grid[i][j] == '1') {
#            parent[i * n + j] = i * n + j;
#            ++count;
#          }
#          rank[i * n + j] = 0;
#        }
#      }
#    }
#
#    public int find(int i) { // path compression
#      if (parent[i] != i) parent[i] = find(parent[i]);
#      return parent[i];
#    }
#
#    public void union(int x, int y) { // union with rank
#      int rootx = find(x);
#      int rooty = find(y);
#      if (rootx != rooty) {
#        if (rank[rootx] > rank[rooty]) {
#          parent[rooty] = rootx;
#        } else if (rank[rootx] < rank[rooty]) {
#          parent[rootx] = rooty;
#        } else {
#          parent[rooty] = rootx; rank[rootx] += 1;
#        }
#        --count;
#      }
#    }
#
#    public int getCount() {
#      return count;
#    }
#  }
#
#  public int numIslands(char[][] grid) {
#    if (grid == null || grid.length == 0) {
#      return 0;
#    }
#
#    int nr = grid.length;
#    int nc = grid[0].length;
#    int num_islands = 0;
#    UnionFind uf = new UnionFind(grid);
#    for (int r = 0; r < nr; ++r) {
#      for (int c = 0; c < nc; ++c) {
#        if (grid[r][c] == '1') {
#          grid[r][c] = '0';
#          if (r - 1 >= 0 && grid[r-1][c] == '1') {
#            uf.union(r * nc + c, (r-1) * nc + c);
#          }
#          if (r + 1 < nr && grid[r+1][c] == '1') {
#            uf.union(r * nc + c, (r+1) * nc + c);
#          }
#          if (c - 1 >= 0 && grid[r][c-1] == '1') {
#            uf.union(r * nc + c, r * nc + c - 1);
#          }
#          if (c + 1 < nc && grid[r][c+1] == '1') {
#            uf.union(r * nc + c, r * nc + c + 1);
#          }
#        }
#      }
#    }
#
#    return uf.getCount();
#  }
#}


## Discuss Solutions:
#########################
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        row = len(grid); col = len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(row) for j in range(col))
        parent = [i for i in range(row*col)]
        
        def find(x):
            if parent[x]!= x:
                return find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
            parent[xroot] = yroot
            self.count -= 1
        
        
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i*col + j
                if j < col-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < row-1 and grid[i+1][j] == '1':
                    union(index, index+col)
        return self.count


def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j -1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


################################################################################


# TODO: union find approach
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        result = 0
        if not grid:
            return result

        num_rows = len(grid)
        num_cols = len(grid[0])
        union_find = UnionFind(grid)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] != '1':
                    continue

                grid[row][col] = '0'
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for x, y in directions:
                    r = row + x
                    c = col + y
                    if not r >= 0 or not c >= 0:
                        continue
                    if grid[r][c] != '1':
                        continue

                    curr_idx = row * num_cols + col
                    next_idx = r * num_cols + c
                    union_find.union(curr_idx, next_idx)
        
        return union_find.get_count()


class UnionFind:
    def __init__(self, grid):
        self.count = 0
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self.parent = [self.num_rows * self.num_cols]
        self.rank = [self.num_rows * self.num_cols]

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                idx_hash = row * self.num_cols + col
                if grid[row][col] == '1':
                    self.parent[idx_hash] = idx_hash
                    self.count += 1
                self.rank[idx_hash] = 0

    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])

        return self.parent[idx]

    def union(self, curr_idx, next_idx):
        curr_root = self.find(curr_idx)
        next_root = self.find(next_idx)
        if curr_root != next_root:
            if self.rank[curr_root] > self.rank[next_root]:
                self.parent[next_root] = curr_root
            elif self.rank[curr_root] < self.rank[next_root]:
                self.parent[curr_root] = next_root
            else:
                self.parent[next_root] = curr_root
                self.rank[curr_root] += 1
            self.count -= 1

    def get_count(self):
        return self.count
