##
#### Scraps
###############

def test_dict():
    test = {
        1 > 0: '1 > 0, true',
        0 > 1: '0 > 1, false',
        10 != 10: '10 == 10, true'
    }

    print(test[True])


def test(hello, world, params):
    hi = 'hi'
    print(locals())

#test('HELLO', 'WORLD', 'PARAMS')


def reverse_string(st):
    string = st.split()
    print(string)

#reverse_string('ypwswhua  dayf ytjitiapg kiot ehthququai lrkhdqgjpd')
#reverse_string('rqywypselytd fhstduupklhfflouhypg  sqalgfeu')


def list_comp(string):
    #print(x for x in string)
    print(' '.join(x for x in string))

#list_comp('hellooo')


def triple_trouble(one, two, three):
    test = zip(one, two, three)
    print(''.join(''.join(x) for x in test))

#triple_trouble("aaa", "bbb", "ccc")

def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += p0 * percent + aug
        years += 1
        
    return years

#print(nb_year(1500, 5, 100, 5000))
#print(nb_year(1500000, 2.5, 10000, 2000000))

test = [1, 2, 3]
test.reverse()

from collections import deque
test_deque = deque([1, 2, 3])
print(test_deque[0])
print(test_deque[-1])
