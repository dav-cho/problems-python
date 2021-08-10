##
#### Moves in squared strings (I) (7 kyu)
#############################################

def vert_mirror(strng):
    arr = strng.split('\n')
    result = []
    for word in arr:
        result.append(word[::-1])

    return '\n'.join(result)
                      
def hor_mirror(strng):
    arr = strng.split('\n')

    return '\n'.join(reversed(arr))
    
def oper(fct, s):
    return fct(s)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(vert_mirror("hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"), "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
        self.assertEqual(vert_mirror("IzOTWE\nkkbeCM\nWuzZxM\nvDddJw\njiJyHF\nPVHfSx"), "EWTOzI\nMCebkk\nMxZzuW\nwJddDv\nFHyJij\nxSfHVP")
        self.assertEqual(hor_mirror("lVHt\nJVhv\nCSbg\nyeCt"), "yeCt\nCSbg\nJVhv\nlVHt")
        self.assertEqual(hor_mirror("njMK\ndbrZ\nLPKo\ncEYz"), "cEYz\nLPKo\ndbrZ\nnjMK")


if __name__ == '__main__':
    unittest.main()

