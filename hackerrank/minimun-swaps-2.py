##
#### Minimum Swaps 2 (medium)
#################################


# i = correct number - 1
# keep track of number?


# nested loops
# time: O(n^2)
# space: O(1)
def minimumSwaps(arr: list[int]) -> int:
    swaps = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] == i + 1:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1

    return swaps


# hash map:
def minimumSwaps(arr: list[int]) -> int:
    swaps = 0

    hash = dict(zip(arr, range(len(arr))))

    for i in range(len(arr)):
        if hash[i + 1] != i:
            hash[arr[i]] = hash[i + 1]
            arr[hash[i + 1]] = arr[i]
            swaps += 1

    # hash = dict(zip(arr, range(1, len(arr) + 1)))

    # for i in range(1, len(arr) + 1):
    #     if hash[i] != i:
    #         hash[arr[i - 1]] = hash[i]
    #         arr[hash[i] - 1] = arr[i - 1]
    #         swaps += 1

    return swaps


# hash = {
#   4: 1    4: 0
#   3: 2    3: 1
#   1: 3    1: 2
#   2: 4    2: 3
# # }

test1 = [4, 3, 1, 2]  # 3
test2 = [2, 3, 4, 1, 5]  # 3
test3 = [1, 3, 5, 2, 4, 6, 7]  # 3


def test(*args):
    test_number = 0

    def run():
        for test in args:
            nonlocal test_number
            test_number += 1
            print(f"test: {test_number}")
            result = minimumSwaps(test)
            print(f"result {test_number}: {result}")

    return run


test(test1, test2, test3)()
