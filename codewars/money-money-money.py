##
#### Money, Money, Money
###################################################


def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        year_interest = principal * interest
        year_tax = year_interest * tax
        principal += year_interest - year_tax
        years += 1

    return years


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(calculate_years(1000, 0.05, 0.18, 1100), 3)
        self.assertEqual(calculate_years(1000,0.01625,0.18,1200), 14)
        self.assertEqual(calculate_years(1000,0.05,0.18,1000), 0)


if __name__ == '__main__':
    unittest.main()

