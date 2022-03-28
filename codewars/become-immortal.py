##
#### BECOME IMMORTAL (1 kyu)
################################


def elder_age(m, n, l, t):
    total = 0
    for row in range(n):
        for col in range(m):
            xor = (col ^ row) - l
            xor = xor if xor > 0 else 0
            total += xor

    return total % t


from pprint import pprint


def elder_age(m, n, l, t):
    result = [[None] * m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            xor = (col ^ row) - l
            xor = xor if xor > 0 else 0
            result[row][col] = xor

    total = sum(sum(x) for x in result)

    return total % t


def elder_age(m, n, l, t):
    total = 0
    for row in range(n):
        curr = 0
        for col in range(m):
            xor = (col ^ row) - l
            # total += xor if xor > 0 else 0

            curr += xor if xor > 0 else 0
        total += curr
        # print(curr)

    print(total % t)

    return total % t


def elder_age(m, n, l, t):
    rows = []
    for row in range(n):
        curr = 0
        for col in range(m):
            xor = (col ^ row) - l
            curr += xor if xor > 0 else 0
        rows.append(curr)

    print(rows)


test = [3, 4, 5, 6, 0, 0, 1, 2]

print(356 - 307)
print(412 - 356)
print(486 - 412)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(elder_age(8, 5, 1, 100), 5)
