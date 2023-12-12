##
#### The Supermarket Queue (6 kyu)
######################################

from collections import deque


def queue_time(customers, n):
    if not customers:
        return 0
    if len(customers) == 1:
        return customers[0]
    if n == 1:
        return sum(customers)
    if n >= len(customers):
        return max(customers)

    tills = customers[:n]
    queue = deque(customers[n:])
    while queue:
        open = tills.index(min(tills))
        tills[open] += queue.popleft()

    return max(tills)


def queue_time(customers, n):
    tills = [0] * n
    for customer in customers:
        tills[tills.index(min(tills))] += customer

    return max(tills)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(queue_time([], 1), 0, "wrong answer for case with an empty queue")
        self.assertEqual(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
        self.assertEqual(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
        self.assertEqual(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
        self.assertEqual(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")


if __name__ == '__main__':
    unittest.main()

