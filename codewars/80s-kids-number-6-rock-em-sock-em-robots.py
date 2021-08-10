##
#### 80's Kids #6: Rock 'Em, Sock 'Em Robots (5 kyu)
########################################################


def fight(robot_1, robot_2, tactics):
    winner = None
    first_attack = "r1" if robot_1["speed"] > robot_2["speed"] else "r2"

    turn = i = j = 0
    while turn < len(robot_1["tactics"]) + len(robot_2["tactics"]):
        if first_attack == "r1":
            robot_2["health"] -= tactics[robot_2["tactics"][i]]
            i += 1

        if robot_2["health"] <= 0:
            winner = robot_1["name"]

def test1():
    print("hello")
    print("world")
    print('hi')


## Tests
############

test1 = (
    {
        "name": "Rocky",
        "health": 100,
        "speed": 20,
        "tactics": ["punch", "punch", "laser", "missile"],
    },
    {
        "name": "Missile Bob",
        "health": 100,
        "speed": 21,
        "tactics": ["missile", "missile", "missile", "missile"],
    },
    {"punch": 20, "laser": 30, "missile": 35},
)  # "Missile Bob has won the fight."

test2 = (
    {
        "name": "Rocky",
        "health": 200,
        "speed": 20,
        "tactics": ["punch", "punch", "laser", "missile"],
    },
    {
        "name": "Missile Bob",
        "health": 100,
        "speed": 21,
        "tactics": ["missile", "missile", "missile", "missile"],
    },
    {"punch": 20, "laser": 30, "missile": 35},
)  # "Rocky has won the fight."

print(fight(*test1))
print(fight(*test2))
