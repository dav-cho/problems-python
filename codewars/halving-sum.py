##
#### Halving Sum (7 kyu)
###################################################


def halving_sum(n): 
    res = 0
    
    while n:
        res += n
        n >>= 1
        
    return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual((), )
        self.assertAlmostEqual((), )


if __name__ == '__main__':
    unittest.main()

