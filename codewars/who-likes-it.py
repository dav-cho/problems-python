##
#### Who likes it? (6 kyu)
##############################


def likes(names):
    length = len(names)
    if not length:
        return "no one likes this"

    if length == 1:
        return f"{names[0]} likes this"

    if length == 2:
        return f"{names[0]} and {names[1]} like this"

    if length == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    if length > 3:
        return f"{names[0]}, {names[1]} and {length - 2} others like this"


def likes(names):
    n = len(names)

    return {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }[min(4, n)].format(*names[:3], others=n - 2)


## Tests
############

print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))

# 'no one likes this'
# 'Peter likes this'
# 'Jacob and Alex like this'
# 'Max, John and Mark like this'
# 'Alex, Jacob and 2 others like this'
