##
#### Return the day (8 kyu)
###############################

def whatday(num):
    return {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }.get(num, 'Wrong, please enter a number between 1 and 7')


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual((), )
        self.assertAlmostEqual((), )


if __name__ == '__main__':
    unittest.main()

