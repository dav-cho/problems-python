##
#### Remove duplicates from list
####################################


def distinct(seq):
    return sorted(set(seq), key=seq.index)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertAlmostEqual(distinct([1]), [1])
        self.assertAlmostEqual(distinct([1, 2]), [1, 2])
        self.assertAlmostEqual(distinct([1, 1, 2]), [1, 2])
        self.assertAlmostEqual(distinct([1, 1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertAlmostEqual(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]), [1, 2, 3, 4, 5, 6, 7])

        self.assertAlmostEqual(distinct([3222243, 3222243, 179599, 3795380, 254353, 3795380, 3795380, 3222243, 3222243, 3795380, 3255393, 3255393, 3795380, 3795380, 3222243, 3795380, 3222243, 179599, 3795380, 3255393, 3795380, 179599, 3222243, 3795380, 3795380, 179599, 179599, 3255393, 3795380, 3795380, 179599, 3795380, 179599, 3795380, 3255393, 3222243, 3795380, 3795380, 3795380, 3222243, 3795380, 3795380, 3255393, 3795380, 3222243, 3222243, 3222243, 3255393, 3255393, 3795380, 3255393, 3255393, 3255393, 3222243, 3795380, 3795380, 3795380, 3222243, 3255393, 3795380, 3222243, 3255393, 3255393, 3795380, 3255393, 3795380, 3795380, 3795380, 3255393, 179599, 3795380, 3795380, 3795380, 3795380, 3222243, 3222243]), [3222243, 179599, 3795380, 254353, 3255393])


if __name__ == '__main__':
    unittest.main()

