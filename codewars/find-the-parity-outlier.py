##
#### Find The Parity Outlier (6 kyu)
########################################


def find_outlier(integers):
    for i in range(3):
        evens = odds = 0

        if integers[i] % 2 == 0:
            evens += 1
        else:
            odds += 1

        find = 1 if evens > odds else 0

    for num in integers:
        if num % 2 == find:
            return num



## Tests
############

print(find_outlier([2, 4, 6, 8, 10, 3])) # 3
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) # 11
print(find_outlier([160, 3, 1719, 19, 11, 13, -21])) # 160

