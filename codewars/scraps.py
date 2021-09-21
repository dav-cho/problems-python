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

creams = 180
a = 65
b = 84
c = 60

######################################################################
