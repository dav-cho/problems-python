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



######################################################################
