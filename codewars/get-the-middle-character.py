##
#### Get the Middle Character (7 kyu)
#########################################


def get_middle(s):
    length = len(s)

    if length % 2 == 0:
        mid = length // 2 - 1
        return s[mid:mid + 2]
    else:
        mid = length // 2
        return s[mid]


## Tests
############

print(get_middle("test"))       # "es"
print(get_middle("testing"))    # "t"
print(get_middle("middle"))     # "dd"
print(get_middle("A"))          # "A"
print(get_middle("of"))         # "of"
