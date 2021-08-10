##
#### scraps-test
####################


def nb_dig(n, d):
    squares = [x * x for x in range(n + 1)]
    count = 0
    for square in squares:
        count += str(square).count(str(d))
        
    return count



## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(nb_dig(5750, 0), 4700)
        self.assertEqual(nb_dig(11011, 2), 9481)
        self.assertEqual(nb_dig(12224, 8), 7733)
        self.assertEqual(nb_dig(11549, 1), 11905)


if __name__ == '__main__':
    unittest.main()

