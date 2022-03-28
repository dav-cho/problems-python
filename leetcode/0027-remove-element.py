##
#### 27. Remove Element (easy)
##################################


## Approach 1: Two Pointers
###############################
# time:
# space:
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


## Approach 2: Two Pointers - when elements to remove are rare
##################################################################
# time:
# space:
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i, length = 0, len(nums)

        while i < length:
            if nums[i] == val:
                nums[i] = nums[length - 1]
                length -= 1
            else:
                i += 1

        return length


## Tests
############

test1 = ([3, 2, 2, 3], 3)  # 2, [2,2,_,_]
test2 = ([0, 1, 2, 2, 3, 0, 4, 2], 2)  # 5, [0,1,4,0,3,_,_,_]
test3 = ([1], 1)  # 0, []
test4 = ([2], 3)  # 1, [2]
test5 = ([3, 3], 3)  # 0, []
test6 = ([], 0)  # 0, []
test7 = ([3, 3], 5)  # 2, [3, 3]
test8 = ([2, 2, 3], 2)  # 1, [3]
test9 = ([0, 4, 4, 0, 4, 4, 4, 0, 2], 4)  # 4, [0, 2, 0, 0]


def test(*args):
    solution = Solution()
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            print("before:", *test)

            result = solution.removeElement(*test)
            count += 1

            print("after:", test[0][:result])
            print("return:", result)

        print("FINISHED")

    return run()


test(test1, test2, test3, test4, test5, test6, test7, test8, test9)
