##
#### Drink about
###################################################


def get_size(w, h, d):
    rect1 = w * h * 2
    rect2 = d * h * 2
    rect3 = w * d * 2
    area = sum([rect1, rect2, rect3])

    volume = w * h * d

    return [area, volume]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEquals(get_size(4, 2, 6), [88,48])
        self.assertEquals(get_size(1, 1, 1), [6,1])
        self.assertEquals(get_size(1, 2, 1), [10,2])
        self.assertEquals(get_size(1, 2, 2), [16,4])
        self.assertEquals(get_size(10, 10, 10), [600,1000])


if __name__ == '__main__':
    unittest.main()

