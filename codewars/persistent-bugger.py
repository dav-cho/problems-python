##
#### Persistent Bugger (6 kyu)
##################################


def persistence(n, count=0):
    if n // 10 == 0:
        return count

    sum = 1
    for digit in list(str(n)):
        sum *= int(digit)

    count += 1

    return persistence(sum, count)


## Tests
############

print(persistence(39), 3)
print(persistence(4), 0)
print(persistence(25), 2)
print(persistence(999), 4)
