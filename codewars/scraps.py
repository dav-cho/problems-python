##
#### Scraps
###############


def test_yield():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


######################################################################

# print(sum([True, True, True, False, False, True, False, True]))

######################################################################

ls = [1, 2, 3, 4]
# print(type(ls) == list)

######################################################################

a = 1
b = 2
c = "3"

#print(not isinstance(a, int))

######################################################################

blah = 'hello'
#print(blah[::-1])

######################################################################

days = [None, 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

######################################################################

## trick to handle negative indexes
#print(-2 % 5)

######################################################################

#import sys
#
#sys.stdout = open('log.txt', 'w')
#
#print('hello world')
#
#sys.stdout.close()

#with open('log.txt', 'a') as file:
#    file.write('\n\n')
#
#    file.write('hello world')

######################################################################

text = "program is fun"
#print(len(text))
#print(text.zfill(15))
#print(text.zfill(20))
#print(text.zfill(10))

######################################################################

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_ll(arr):
    head = ListNode(arr[0])
    prev = head
    for num in arr[1:]:
        new = ListNode(num)
        prev.next = new
        prev = prev.next
    return head

def print_ll(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)
    return res


head = build_ll([1,2,3,4])
#print_ll(head)

#head = build_ll([])
#self.print_ll(head)
#
#head = build_ll([1])
#self.print_ll(head)

######################################################################

COLORS = set("RGB")

def triangle(row):
    while len(row)>1:
        row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row

######################################################################

import operator

def logical_calc(array, op):
    ops = {
        'AND': operator.and_,
        'OR': operator.or_,
        'XOR': operator.xor
    }
    
    return reduce(ops[op], array)

######################################################################

def halving_sum(n): 
    res = 0
    
    while n:
        res += n
        n >>= 1
        
    return res

def halving_sum(n): 
    res = n
    i = 2
    while n // i > 0:
        res += n // i
        i *= 2
    
    return res

######################################################################

def power_of_two(x):
    return x != 0 and ((x & (x - 1)) == 0)

######################################################################

def my_languages(results):
    return sorted((l for l,r in results.items() if r>=60), reverse=True, key=results.get)

######################################################################

def presses(phrase):
    return sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button)

######################################################################

a = 15
b = 14
c = 13
d = 13
e = 8

total = sum([a, b, c, d, e])

######################################################################

def count_one(n):
    count = 0

    while n:
        n = n & (n - 1)
        count += 1
    
    return count


def get_sum(a, b):
    if b == 0:
        return a

    print('^', a ^ b)
    print('&', a & b)

    return get_sum(a ^ b, (a & b) << 1)

def missing_number(nums):
    res = 0

    for i, num in enumerate(nums):
        res ^= i
        res ^= num

    res ^= len(nums)

    return res

######################################################################

def bitwise_not(arr):
    for num in arr:
        print(f"""
            num:    {num}
            ~:      {~num}
            math:   {5 - num - 1}
            ~math:  {~num + 5}""")

#bitwise_not(range(10))

######################################################################

from pprint import pprint


def rotate(matrix):
    N = len(matrix)

    pprint(matrix)

    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    pprint(matrix)

######################################################################

a = [[1,4,7],
     [2,5,8],
     [3,6,9]]

b = [[1,2,3],
     [4,5,6],
     [7,8,9]]

######################################################################

#for i in range(5):
#    print('&:', i & 1)
#    print('1-:', 1 - i & 1)

######################################################################

a = {1, 2, 3}
b = {3, 4, 5}
c = {5, 6, 7}

#print(a | b)
#print(b | c)
#print(a | c)
#print(a | b | c)

#print(set(range(1, 10)) - set(range(1, 6)))

######################################################################

a = int('00101100', 2)
b = bin(44)
#print(a)
#print(b)

c = bin(123)
d = f'{123:08b}'
e = '{0:08b}'.format(123)
#print(c)
#print(d)
#print(e)

f = int('00101100', 2)
#g = f"{00101100:d}"
#print(f)
#print(g)

######################################################################

converted = 0

for i, val in enumerate(d[::-1]):
    #print(f'val{i}:', val)
    #print('&:', int(val) & 1)
    #print('<<:', 1 << i)
    #print('& <<:', int(val) & (1 << i))

    if int(val) & 1 == 1:
        converted += 1 << i
        #print('converted:', converted)

######################################################################

read = 4
write = 2
execute = 1

my_permission = 0
my_permission = read | write | execute
#print(my_permission)

my_permission = 0
my_permission = my_permission | read | write | execute
#print(my_permission)

my_permission = 0
my_permission = my_permission | read | write
#print(my_permission)

message = 'yes' if my_permission & read else 'no'
#print(message)
message = 'yes' if my_permission & write else 'no'
#print(message)
message = 'yes' if my_permission & execute else 'no'
#print(message)

######################################################################

#print('15pcs:', 9.75 / 15)
#print('35pcs:', 21.70 / 35)
#print('70pcs:', 25.90 / 70)
#print('90pcs:', 32.40 / 90)
#print('110pcs:', 38.50 / 110)
#print('120pcs:', 25.90 * 2 / 140)
#print()

#print('cobalt:', 45.50 / 70)
#print('coffee', 51.70 / 110)

######################################################################

a = [1, 2, 3]
b = [3, 4, 5]

from collections import Counter

counts_a = Counter(a)
counts_b = Counter(b)
#print(list(counts_a & counts_b))

######################################################################

