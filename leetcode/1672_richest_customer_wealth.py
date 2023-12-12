"""
1672. Richest Customer Wealth (easy)
"""

import unittest
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totals = [0] * len(accounts)
        for customer in range(len(accounts)):
            for bank in range(len(accounts[customer])):
                totals[customer] += accounts[customer][bank]
        return max(totals)


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totals = [0] * len(accounts)
        for i, customer in enumerate(accounts):
            for bank in range(len(customer)):
                totals[i] += customer[bank]
        return max(totals)


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)


## Tests
########################################################################################


class Test(unittest.TestCase):
    def test_cases(self):
        for t, e in [
            ([[1, 2, 3], [3, 2, 1]], 6),
            ([[1, 5], [7, 3], [3, 5]], 10),
            ([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
        ]:
            self.assertEqual(Solution().maximumWealth(t), e)


if __name__ == "__main__":
    unittest.main()
