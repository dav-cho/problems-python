##
#### Sudoku Solver (3 kyu)
###################################################

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    return puzzle


from collections import deque


def sudoku(puzzle):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subs = [set() for _ in range(9)]
    queue = deque()
    
    for row in range(9):
        for col in range(9):
            num = puzzle[row][col]
            
            if num == 0:
                queue.append((row, col))
            else:
                sub = row // 3 * 3 + col // 3
                
                rows[row].add(num)
                cols[col].add(num)
                subs[sub].add(num)
                
    while queue:
        row, col = queue.popleft()
        sub = row // 3 * 3 + col // 3
        use = set(range(1, 10)) - (rows[row] | cols[col] | subs[sub])
        
        if len(use) == 1:
            num = use.pop()
            puzzle[row][col] = num
            rows[row].add(num)
            cols[col].add(num)
            subs[sub].add(num)
        else:
            queue.append((row, col))

    return puzzle


def sudoku(puzzle):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subs = [set() for _ in range(9)]
    queue = deque()
    
    for row in range(9):
        for col in range(9):
            num = puzzle[row][col]
            
            if num == 0:
                queue.append((row, col))
            else:
                sub = row // 3 * 3 + col // 3
                
                rows[row].add(num)
                cols[col].add(num)
                subs[sub].add(num)
                
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] != 0:
                continue

            row, col = queue.popleft()
            sub = row // 3 * 3 + col // 3
            use = set(range(1, 10)) - (rows[row] | cols[col] | subs[sub])
            
            if len(use) == 1:
                puzzle[row][col] = use.pop()
                
                return sudoku(puzzle)
        
    return puzzle


def sudoku(puzzle):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    subs = [set() for _ in range(9)]
    queue = deque()
    
    for row in range(9):
        for col in range(9):
            num = puzzle[row][col]
            
            if num == 0:
                queue.append((row, col))
            else:
                sub = row // 3 * 3 + col // 3
                
                rows[row].add(num)
                cols[col].add(num)
                subs[sub].add(num)
                
    while queue:
        row, col = queue.popleft()
        sub = row // 3 * 3 + col // 3
        use = set(range(1, 10)) - (rows[row] | cols[col] | subs[sub])
        
        if len(use) == 1:
            puzzle[row][col] = use.pop()
            
            return sudoku(puzzle)
        
    return puzzle


def sudoku(puzzle):
    for row, col in [(x, y) for x in range(9) for y in range(9) if not puzzle[x][y]]:
        r = row // 3 * 3
        c = col // 3 * 3

        use = set(range(1, 10)) - ({puzzle[row][y] for y in range(9)} | {puzzle[x][col] for x in range(9)} | {puzzle[r + x][c + y] for x in range(3) for y in range(3)})

        if len(use) == 1:
            puzzle[row][col] = use.pop()

            return sudoku(puzzle)

    return puzzle


def sudoku(puzzle):
    for row, col in [(x, y) for x in range(9) for y in range(9) if not puzzle[x][y]]:
        r = row // 3 * 3
        c = col // 3 * 3
            
        check_row = {puzzle[row][y] for y in range(9)}
        check_col = {puzzle[x][col] for x in range(9)}
        check_sub = {puzzle[r + x][c + y] for x in range(3) for y in range(3)}
        use = set(range(1, 10)) - (check_row | check_col | check_sub)

        if len(use) == 1:
            puzzle[row][col] = use.pop()
            
            return sudoku(puzzle)
        
    return puzzle


def sudoku(puzzle):
    for row, col in [(x, y) for x in range(9) for y in range(9) if not puzzle[x][y]]:
        r = row // 3 * 3
        c = col // 3 * 3
            
        use = set(range(1, 10)) - ({puzzle[row][y] for y in range(9)} | {puzzle[x][col] for x in range(9)} | {puzzle[r + x][c + y] for x in range(3) for y in range(3)})

        if len(use) == 1:
            puzzle[row][col] = use.pop()
            
            return sudoku(puzzle)
        
    return puzzle


def sudoku(puzzle):
    for row, col in [(r, c) for r in range(9) for c in range(9) if not puzzle[r][c]]:
            
        rr, cc = (row // 3) * 3, (col // 3) * 3
            
        use = {1,2,3,4,5,6,7,8,9} - ({puzzle[row][c] for c in range(9)} | {puzzle[r][col] for r in range(9)} | {puzzle[rr+r][cc+c] for r in range(3) for c in range(3)})

        if len(use) == 1:
            puzzle[row][col] = use.pop()
            return sudoku(puzzle)
    return puzzle


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        puzzle = [[5,3,0,0,7,0,0,0,0],
                  [6,0,0,1,9,5,0,0,0],
                  [0,9,8,0,0,0,0,6,0],
                  [8,0,0,0,6,0,0,0,3],
                  [4,0,0,8,0,3,0,0,1],
                  [7,0,0,0,2,0,0,0,6],
                  [0,6,0,0,0,0,2,8,0],
                  [0,0,0,4,1,9,0,0,5],
                  [0,0,0,0,8,0,0,7,9]]
        solution = [[5,3,4,6,7,8,9,1,2],
                    [6,7,2,1,9,5,3,4,8],
                    [1,9,8,3,4,2,5,6,7],
                    [8,5,9,7,6,1,4,2,3],
                    [4,2,6,8,5,3,7,9,1],
                    [7,1,3,9,2,4,8,5,6],
                    [9,6,1,5,3,7,2,8,4],
                    [2,8,7,4,1,9,6,3,5],
                    [3,4,5,2,8,6,1,7,9]]
        self.assertEqual(sudoku(puzzle), solution)


if __name__ == '__main__':
    unittest.main()

