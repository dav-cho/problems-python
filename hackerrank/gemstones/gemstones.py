##
#### Gemstones (easy)
#########################


def gemstones(arr):
    sets = []

    for word in arr:
        sets.append(set(word))

    return len(sets[0].intersection(*sets[1:]))


def gemstones2(arr):
    pass


## Tests
############

test1 = ['abc', 'abc', 'bc']            # 2
test2 = ['abcdde', 'baccd', 'eeabg']    # 2

print(gemstones(test1))
print(gemstones(test2))

print(gemstones2(test1))
print(gemstones2(test2))
