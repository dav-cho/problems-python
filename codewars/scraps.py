##
#### Scraps
###############

def test_yield():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

#for value in test_yield():
#    print(value)

node = '0123'

def test(param):
    for i in range(4):
        digit = int(node[i])

        for d in (-1, 1):
            y = (digit + d) % 10
            yield node[:i] + str(y) + node[i + 1:]

#for j in test(node):
#    print(j)


def perfect_squares(n):
    for num in range(n + 1):
        root = int(num ** 0.5)
        if root ** 2 == num:
            yield num

for num in perfect_squares(20):
    print(num)

