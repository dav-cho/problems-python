input_file = open(
    "/Users/dav/CODING/problems/python/adventofcode/2020/01_report_repair.txt", "r"
)
inputs = input_file.read().splitlines()


def report_repair1(entries: int) -> int:
    compliments = set()

    for entry in entries:
        entry = int(entry)
        compliment = 2020 - entry

        if compliment in compliments:
            return compliment * entry

        compliments.add(entry)

    # for i in range(len(entries)):
    #     for j in range(i + 1, len(entries)):
    #         if int(entries[i]) == 2020 - int(entries[j]):
    #             return int(entries[i]) * int(entries[j])


result1 = report_repair1(inputs)
print(result1)  # 121396


def report_repair2(entries):
    compliments = set()

    for i, entry in enumerate(entries):
        entry = int(entry)

        for j in range(i + 1, len(entries)):
            other = int(entries[j])
            compliment = 2020 - entry - other

            if compliment in compliments and other in compliments:
                return compliment * entry * other

            compliments.add(entry)
            compliments.add(other)

    # for i in range(len(entries)):
    #     for j in range(i + 1, len(entries)):
    #         for k in range(j + 1, len(entries)):
    #             if int(entries[i]) == 2020 - int(entries[j]) - int(entries[k]):
    #                 return int(entries[i]) * int(entries[j]) * int(entries[k])


result2 = report_repair2(inputs)
print(result2)  # 73616634
