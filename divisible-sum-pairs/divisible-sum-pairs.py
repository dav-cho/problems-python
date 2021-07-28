##
#### Divisible Sum Pairs (easy)
###################################


def divisible_sum_pairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i < j and not (ar[i] + ar[j]) % k:
                count += 1

    return count


## Tests
############

test1 = (6, 3, [1, 3, 2, 6, 1, 2])  # 5

print(divisible_sum_pairs(*test1))


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            result = divisible_sum_pairs(*test)
            print(result)

    return run()


#test(test1, test2)
