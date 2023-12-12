##
#### Snail (4 kyu)
###################################################

def snail(snail_map):
    rows = len(snail_map)
    cols = len(snail_map[0])

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row = col = i = 0
    result = []
    seen = set()
    for _ in range(rows * cols):
        result.append(snail_map[row][col])
        seen.add((row, col))

        r = row + directions[i][0]
        c = col + directions[i][1]
        if 0 <= r < rows and 0 <= c < cols and (r, c) not in seen:
            row = r
            col = c
        else:
            i = (i + 1) % 4
            row += directions[i][0]
            col += directions[i][1]

    return result


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):

        array = [[1,2,3],
                [4,5,6],
                [7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(snail(array), expected)


        array = [[1,2,3],
                 [8,9,4],
                 [7,6,5]]
        expected = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(snail(array), expected)

if __name__ == '__main__':
    unittest.main()

