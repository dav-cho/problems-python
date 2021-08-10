##
#### Rotate for a max (7 kyu)
###################################################


def max_rot(n):
    rotations = [n]
    n = str(n)

    for i in range(len(n)):
        keep = n[:i]
        rotate = n[i:]
        n = keep + rotate[1:] + rotate[0]
        rotations.append(int(n))

    return max(rotations)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(max_rot(38458215), 85821534)
        self.assertEqual(max_rot(195881031), 988103115)
        self.assertEqual(max_rot(896219342), 962193428)
        self.assertEqual(max_rot(69418307), 94183076)

        self.assertEqual(max_rot(507992495), 507992495)
        self.assertEqual(max_rot(84005278654009), 84005278654009)
        self.assertEqual(max_rot(51564279810300), 51564279810300)


if __name__ == '__main__':
    unittest.main()

