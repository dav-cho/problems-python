##
#### Insane Coloured Triangles (2 kyu)
##########################################


def triangle(row):
    colors = set('RGB')

    while len(row) > 1:
        row = [a if a == b else (colors - {a, b}).pop() for a, b in zip(row, row[1:])]

    return row[0]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(triangle('B'), 'B'),
        self.assertEqual(triangle('GB'), 'R'),
        self.assertEqual(triangle('RRR'), 'R'),
        self.assertEqual(triangle('RGBG'), 'B'),
        self.assertEqual(triangle('RBRGBRB'), 'G'),
        self.assertEqual(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')


if __name__ == '__main__':
    unittest.main()

