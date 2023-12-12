##
#### Square Every Digit (7 kyu)
###################################

def square_digits(num):
    return int(''.join([str(int(x) ** 2) for x in str(num)]))


## Tests
############

print(square_digits(9119), 811181)
print(square_digits(0), 0)

