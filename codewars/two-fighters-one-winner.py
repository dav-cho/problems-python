##
#### Two fighters, one winner. (7 kyu)
##########################################

class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self):
        return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):
    one = fighter1 if fighter1.name == first_attacker else fighter2
    two = fighter2 if one == fighter1 else fighter1
    winner = None

    while True:
        two.health -= one.damage_per_attack
        if two.health <= 0:
            winner = one
            break

        one.health -= two.damage_per_attack
        if one.health <= 0:
            winner = two
            break

    return winner.name



## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew"), "Lew")
        self.assertEqual(declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Harry"),"Harry")
        self.assertEqual(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harry"),"Harald")
        self.assertEqual(declare_winner(Fighter("Harald", 20, 5), Fighter("Harry", 5, 4), "Harald"),"Harald")
        self.assertEqual(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Jerry"), "Harald")
        self.assertEqual(declare_winner(Fighter("Jerry", 30, 3), Fighter("Harald", 20, 5), "Harald"),"Harald")



if __name__ == '__main__':
    unittest.main()

