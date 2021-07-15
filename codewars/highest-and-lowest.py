##
#### Highest and Lowest (7 kyu)
###################################

def high_and_low(numbers):
    high, low = float('-inf'), float('inf')

    for num in numbers.split(' '):
        num = int(num)

        if num > high:
            high = num
        if num < low:
            low = num

    return f'{high} {low}'


def high_and_low(numbers):
    arr = [int(n) for n in numbers.split(' ')]
    
    return '%i %i' % (max(arr), min(arr))

## Tests
############

print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"

