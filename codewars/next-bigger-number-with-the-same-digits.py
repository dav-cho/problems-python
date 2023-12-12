##
#### Next bigger number with the same digits (4 kyu)
########################################################


def next_bigger(n):
    n = str(n)

    if "".join(sorted(n, reverse=True)) == n:
        return -1

    i = len(n) - 1
    while not n[i] > n[i - 1]:
        i -= 1

    back = sorted(n[i:])
    for j, digit in enumerate(back):
        if digit > n[i - 1]:
            sub = digit
            back[j] = n[i - 1]
            return int(n[: i - 1] + sub + "".join(back))


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(next_bigger(12), 21)
        self.assertEqual(next_bigger(513), 531)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(414), 441)
        self.assertEqual(next_bigger(144), 414)

        self.assertEqual(next_bigger(9876543210), -1)


if __name__ == "__main__":
    unittest.main()
