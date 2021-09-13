##
#### The observed PIN (4 kyu)
#################################

def get_pins(observed):
    #numpad = [
    #    [1, 2, 3], 
    #    [4, 5, 6],
    #    [7, 8, 9],
    #    [None, 0, None],
    #]
    #dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def backtrack(first=0):
        if first == n:
            pass

        for i in range(start, n):
            pass

    n = len(observed)
    dirs = [1, -1, 3, -3]
    adj_list = [[] for _ in range(n)]

    for i, num in enumerate(observed):
        adj_list[i] = [num]
        for dir in dirs:
            adj_list[i].append(int(num) + dir)

    res = []
    for i in range(n):
        for j in range(i, n):
            pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        #self.assertEqual(get_pins('8'), ['5','7','8','9','0']),
        self.assertEqual(get_pins('11'),["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
        self.assertEqual(get_pins('369'), ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])


if __name__ == '__main__':
    unittest.main()

