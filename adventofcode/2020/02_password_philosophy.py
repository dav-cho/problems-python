input_file = open(
    "/Users/dav/CODING/problems/python/adventofcode/2020/02_password_philosophy.txt",
    "r",
)
inputs = input_file.read().splitlines()


def password_philosophy1(passwords):
    valid_count = 0

    for i in range(len(passwords)):
        temp = passwords[i].split(":")
        password = temp[1]
        policy = temp[0].split(" ")
        limits, letter = policy[0].split("-"), policy[1]
        # print(limits, letter)
        # print(password)

        count = 0
        for char in password:
            if char is letter:
                count += 1
        if count >= int(limits[0]) and count <= int(limits[1]):
            valid_count += 1

    return valid_count


result1 = password_philosophy1(inputs)
print(result1)


def password_philosophy2(passwords):
    valid_count = 0

    for i in range(len(passwords)):
        # for i in range(2):
        temp = passwords[i].split(":")
        password = temp[1]
        policy = temp[0].split(" ")
        limits, letter = policy[0].split("-"), policy[1]
        low = int(limits[0]) - 1
        high = int(limits[1]) - 1
        # print(low, high, letter, password)
        # print(password[low], password[high])

        if password[low] == letter and password[high] != letter:
            continue
        elif password[low] == letter and password[high] == letter:
            continue
        elif password[low] == letter or password[high] == letter:
            valid_count += 1
            # print("valid")

    return valid_count


result2 = password_philosophy2(inputs)
print(result2)
