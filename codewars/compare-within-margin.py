##
#### Compare within margin (8 kyu)
######################################


def close_compare(a, b, margin=0):
    return 0 if margin and margin >= abs(a - b) else (a > b) - (a < b)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            (),
        )
        self.assertAlmostEqual(
            (),
        )


if __name__ == "__main__":
    unittest.main()
