##
#### 80's Kids #6: Rock 'Em, Sock 'Em Robots (5 kyu)
########################################################


def fight(robot_1, robot_2, tactics):
    a = robot_1 if robot_1['speed'] >= robot_2['speed'] else robot_2
    b = robot_2 if a is robot_1 else robot_1

    i = 0
    length = max(len(a['tactics']), len(b['tactics']))
    while i < length:
        a_damage = tactics[a['tactics'][i]] if a['tactics'][i] else 0
        b_damage = tactics[b['tactics'][i]] if b['tactics'][i] else 0

        b['health'] -= a_damage
        if b['health'] <= 0:
            return f"{a['name']} has won the fight."
        a['health'] -= b_damage
        if a['health'] <= 0:
            return f"{b['name']} has won the fight."

        i += 1

    if a['health'] == b['health']:
        return 'The fight was a draw.'
    winner = a['name'] if a['health'] > b['health'] else b['name']
    return f"{winner} has won the fight."


def fight(robot_1, robot_2, tactics):
    a, b = (robot_1, robot_2) if robot_1['speed'] >= robot_2['speed'] else (robot_2, robot_1)

    while a['health'] > 0:
        if a['tactics']:
            b['health'] -= tactics[a['tactics'].pop()]
        elif not b['tactics']:
            break
        a, b = b, a

    if a['health'] == b['health']:
        return 'The fight was a draw.'
    return f"{(a if b['health'] < a['health'] else b)['name']} has won the fight."


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        robot_1 = {"name": "Rocky", "health": 100, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
        robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
        tactics = {"punch": 20, "laser": 30, "missile": 35}
        self.assertEqual(fight(robot_1, robot_2, tactics), "Missile Bob has won the fight.")
        
        robot_1 = {"name": "Rocky", "health": 200, "speed": 20, "tactics": ["punch", "punch", "laser", "missile"] }
        robot_2 = {"name": "Missile Bob", "health": 100, "speed": 21, "tactics": ["missile", "missile", "missile", "missile"]}
        tactics = {"punch": 20, "laser": 30, "missile": 35}
        self.assertEqual(fight(robot_1, robot_2, tactics), "Rocky has won the fight.")


if __name__ == '__main__':
    unittest.main()

