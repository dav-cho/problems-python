##
#### Tribonacci Sequence (6 kyu)
####################################

def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    for _ in range(n - 3):
        next = sum(signature[-3:])
        signature.append(next)

    return signature


def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


test1 = ([1, 1, 1], 10)
test2 = ([0, 0, 1], 10)
test3 = ([0, 1, 1], 10)
test4 = ([1, 0, 0], 10)
test5 = ([0, 0, 0], 10)
test6 = ([1, 2, 3], 10)
test7 = ([3, 2, 1], 10)
test8 = ([1, 1, 1], 1)

tests = (
    test1,
    test2,
    test3,
    test4,
    test5,
    test6,
    test7,
    test8,
)


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            result = tribonacci(*test)

            #print('dice:', test)
            #print('result:', result)
            print(result)

    return run()


test(*tests)

