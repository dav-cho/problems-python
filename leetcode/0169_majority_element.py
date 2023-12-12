##
#### 169. Majority Element (easy)
#####################################


from collections import Counter


def majorityElement(nums: list[int]) -> int:
    count = Counter(nums)

    for num in count:
        if count[num] > len(nums) // 2:
            return num
