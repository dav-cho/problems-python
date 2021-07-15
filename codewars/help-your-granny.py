##
#### Help Your Granny! (5 kyu)
##################################

from math import sqrt, cos, acos, degrees, radians


def pythagorean(b, c):
    return sqrt(c ** 2 - b ** 2)


# cos(angle) = b / c
# angle = acos(b / c)
def find_angle(b, c):
    return degrees(acos(b / c))


# distance = sqrt of b^2 + c^2 - 2(bc) * cos(angle)
def find_dist(b, c, angle):
    result = b ** 2 + c ** 2 - 2 * b * c * cos(radians(angle))
    return sqrt(result)


#print(pythagorean(110, 150))

blah = find_angle(80, 100) + find_angle(100, 110)
print(blah)
print('dist', find_dist(80, 110, 75))
print(53 + 88.72 + 102 + 60 + 150)


# total += first and last
# find total distances between points of first and last perimeter
def tour(friends: list[str], towns: list[list[str]], distances: dict):
    valid_towns = set(town[0] for town in towns)
    char = list(distances)[0][0]
    
    first, last = 0, len(friends) - 1
    while friends[first] not in valid_towns:
        first += 1
    while friends[last] not in valid_towns:
        last -= 1
        
    start = distances[char + friends[first][1]]
    end = distances[char + friends[last][1]]
    total = start + end
    
    for i in range(first, last):
        curr, next = int(friends[i][1]), int(friends[i + 1][1])
        
        if next - curr > 1:
            angle = 0
            
            while curr < next:
                b = distances[char + str(curr)]
                c = distances[char + str(curr + 1)]
                angle += find_angle(b, c)
                curr += 1
                
            print(angle)
            x, y = distances[char + str(curr)], distances[char + str(next)]
            total += find_dist(x, y, angle)
            
        else:
            b = distances[char + str(curr)]
            c = distances[char + str(next)]
            total += pythagorean(b, c)
        
    return int(total)


## tests
############


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            friends, towns, distances = test
            print("~ test", count)
            print("friends", friends)
            print("towns", towns)
            print("distances", distances)

            result = tour(*test)

            print("result:", result)

    return run()


test1 = (
    ["A1", "A2", "A3", "A4", "A5"],
    [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]],
    {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
) # 889
test2 = (
    ['A1', 'A2', 'A3', 'A4', 'A5'],
    [['A1', 'X1'], ['A2', 'X2'], ['A3', 'X3'], ['A4', 'X4'], ['A5', 'X5']],
    {'X1': 100.0, 'X2': 200.0, 'X3': 250.0, 'X4': 300.0, 'X5': 320.0}
) # 1020
test3 = (
    ['B1', 'B2'],
    [['B1', 'Y1'], ['B2', 'Y2'], ['B3', 'Y3'], ['B4', 'Y4'], ['B5', 'Y5']],
    {'Y1': 50.0, 'Y2': 70.0, 'Y3': 90.0, 'Y4': 110.0, 'Y5': 150.0}
) # 168
test8 = (
    ['B1', 'B2', 'B4', 'B5', 'B6'],
    [['B1', 'Y1'], ['B2', 'Y2'], ['B3', 'Y3'], ['B4', 'Y4'], ['B5', 'Y5']],
    {'Y1': 60.0, 'Y2': 80.0, 'Y3': 100.0, 'Y4': 110.0, 'Y5': 150.0}
) # 440

#test(test1, test2, test3, test8)
test(test8)

