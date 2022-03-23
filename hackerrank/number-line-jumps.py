##
#### Number Line Jumps (easy)
#################################


def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 < v2:
        return "NO"

    if v1 != v2 and (x2 - x1) % (v2 - v1) == 0:
        return "YES"

    return "NO"


## Tests
############

test1 = [0, 3, 4, 2]        # YES
test2 = [0, 2, 5, 3]        # NO
test3 = [21, 6, 47, 3]      # NO

print(kangaroo(*test1))
print(kangaroo(*test2))
print(kangaroo(*test3))
