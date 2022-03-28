##
#### 1089. Duplicate Zeros (easy)
#####################################


## nested loops
###################
# time: O(n^2)
# space: O(1)
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0:
                for j in range(len(arr) - 1, i, -1):
                    arr[j] = arr[j - 1]

                arr[i + 1] = 0
                i += 2

            else:
                i += 1


## two pass
###############
# time: O(n)
# space: O(1)
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        zeroes, i, last = 0, 0, len(arr) - 1

        while i <= last:
            if arr[i] == 0:
                if i == last:
                    arr[-1] = 0
                    last -= 1
                    break

                zeroes += 1
                last -= 1

            i += 1

        for j in range(last, -1, -1):
            if arr[j] == 0:
                arr[j + zeroes] = 0
                zeroes -= 1
                arr[j + zeroes] = 0
            else:
                arr[j + zeroes] = arr[j]


## Tests
############

test1 = [1, 0, 2, 3, 0, 4, 5, 0]
test2 = [1, 2, 3]
test3 = [8, 4, 5, 0, 0, 0, 0, 7]
test4 = [1, 5, 2, 0, 6, 8, 0, 6, 0]
#        0  1  2  3  4  5  6  7  8

solution = Solution()

solution.duplicateZeros(test1)
print(test1)  # [1,0,0,2,3,0,0,4]

solution.duplicateZeros(test2)
print(test2)  # [1,2,3]

solution.duplicateZeros(test3)
print(test3)  # [8, 4, 5, 0, 0, 0, 0, 0]

solution.duplicateZeros(test4)
print(test4)  # [1, 5, 2, 0, 0, 6, 8, 0, 0]
