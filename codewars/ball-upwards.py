##
#### Ball Upwards (6 kyu)
#############################

# 9.8m/s^2 = 0.0098km/s^2
# km/h = 1000m/3600s
# height = (v * t) - (0.5 * g * t * t)

def max_ball(v):
    v = v / 36
    g = 0.098
    h = mx = t = 0

    while True:
        h = (v * t) - (0.5 * g * t * t)
        if h < mx:
            break
        mx = h
        t += 1

    return t - 1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(max_ball(25), 7)
        self.assertEqual(max_ball(37), 10)
        self.assertEqual(max_ball(45), 13)
        self.assertEqual(max_ball(99), 28)
        self.assertEqual(max_ball(85), 24)

        self.assertEqual(max_ball(15), 4)
        self.assertEqual(max_ball(90), 25)

if __name__ == '__main__':
    unittest.main()

