##
#### Sum of Digits / Digital Root (6 kyu)
#############################################


def digital_root(n):
    if n == 0:
        return 0

    rest = n // 10
    digit = n % 10
    print(digit, rest)

    return digit + (digital_root(rest))


## Tests
############

print(digital_root(16)) # 7
print(digital_root(942)) # 6
print(digital_root(132189)) # 6
print(digital_root(493193)) # 2

