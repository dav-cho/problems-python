##
#### Day of the Programmer (easy)
#####################################

from datetime import datetime


def day_of_programmer(year):
    day = 256

    if year == 1918:
        day += 13

    if year < 1918:
        if not year % 400 or (not year % 4 and year % 100):
            day += 1
        if not year % 4:
            day -= 1

    date = datetime.strptime(f"{year} {day}", "%Y %j")

    return date.strftime("%d.%m.%Y")


## Tests
############

test0 = 2017  # 13.09.2017
test1 = 2016  # 12.09.2016
test11 = 1916  # 12.09.1916
test59 = 1918  # 26.09.1918
test60 = 1800  # 12.09.1800


def test(*args):
    def run():
        for test in args:
            print(f"{test=}".split("=")[1])
            print(day_of_programmer(test))

    return run()


test(test0, test1, test11, test59, test60)
