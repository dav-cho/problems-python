##
#### 200. Number of Islands (medium)
########################################


## dfs
##########
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        result = 0
        if not grid:
            return result

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    result += 1
                    self.dfs(row, col, grid)

        return result

    def dfs(self, row, col, grid):
        if not 0 <= row < len(grid):
            return
        if not 0 <= col < len(grid[0]):
            return
        if grid[row][col] == "0":
            return

        grid[row][col] = "0"
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
            if grid[row][col] == "0":
                return

            grid[row][col] = "0"
            for direction in directions:
                dfs(row + direction[0], col + direction[1])

        result = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
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
                if grid[row][col] != "1":
                    continue

                result += 1
                grid[row][col] = "0"
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
                        if grid[r][c] != "1":
                            continue

                        grid[r][c] = "0"
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
                if grid[row][col] != "1":
                    continue

                result += 1
                grid[row][col] = "0"
                queue = [(row, col)]
                while queue:
                    r, c = queue.pop()
                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for x, y in directions:
                        if not 0 <= r + x < num_rows:
                            continue
                        if not 0 <= c + y < num_cols:
                            continue
                        if grid[r + x][c + y] != "1":
                            continue

                        grid[r + x][c + y] = "0"
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
                if grid[row][col] != "1":
                    continue

                result += 1
                grid[row][col] = "0"
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
                        if grid[r + x][c + y] != "1":
                            continue

                        grid[r + x][c + y] = "0"
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
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]  # 1
test2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]  # 3
test3 = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]  # 1

tests = [
    test1,  # 1
    test2,  # 3
    test3,  # 1
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
