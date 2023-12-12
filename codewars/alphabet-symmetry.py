##
#### Alpahbet symmetry (7 kyu)
##################################


def solve(arr):
    res = []
    for word in arr:
        word = word.lower()
        count = 0
        for i in range(len(word)):
            if ord(word[i]) - 96 == i + 1:
                count += 1
        res.append(count)
                
    return res


#def solve(arr):
    return [ sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr ]



## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(solve(["abode","ABc","xyzD"]),[4,3,1])
        self.assertEqual(solve(["abide","ABc","xyz"]),[4,3,0])
        self.assertEqual(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]),[6,5,7])
        self.assertEqual(solve(["encode","abc","xyzD","ABmD"]),[1, 3, 1, 3])


if __name__ == '__main__':
    unittest.main()

