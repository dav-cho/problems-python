# Merge Sort

## Intuition

There are two approaches to implement the merge sort algorithm: **top down** or **bottom up**. Here, we will explain the top down approach as it can be implemented naturally using recursion.

The merge sort algorithm can be divided into three steps, like all divide-and-conquer algorithms:

1. Divide the given unsorted list into several sublists.  (Divide)
2. Sort each of the sublists recursively.  (Conquer)
3. Merge the sorted sublists to produce new sorted list.  (Combine)

## Top-down Approach

1. In the first step, we divide the list into two sublists.  (Divide)
2. Then in the next step, we recursively sort the sublists in the previous step.  (Conquer)
3. Finally we merge the sorted sublists in the above step repeatedly to obtain the final list of sorted elements.  (Combine)

### Implementation

```python
def merge_sort(nums):
    # bottom cases: empty or list of a single element.
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums) / 2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1
    
    # append what is remained in either of the lists
    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])
    
    return ret
```

## Bottom-up Approach

In the **bottom up** approach, we divide the list into sublists of a single element at the beginning. Each of the sublists is then sorted already. Then from this point on, we merge the sublists two at a time until a single list remains.

## Complexity

The overall time complexity of the merge sort algorithm is {O(N \log{N})}O(NlogN), where {N}N is the length of the input list. To calculate the complexity, we break it down to the following steps:

We recursively divide the input list into two sublists, until a sublist with single element remains. This dividing step computes the midpoint of each of the sublists, which takes {O(1)}O(1) time. This step is repeated NN times until a single element remains, therefore the total time complexity is O(N)O(N).
 
Then, we repetitively merge the sublists, until one single list remains. The recursion tree in Fig. 1 or Fig. 2 above is useful for visualizing how the recurrence is iterated. As shown in the recursion tree, there are a total of NN elements on each level. Therefore, it takes O({N})O(N) time for the merging process to complete on each level. And since there are a total of \log{N}logN levels, the overall complexity of the merge process is O({N \log{N}})O(NlogN).
Taking into account the complexity of the above two parts in the merge sort algorithm, we conclude that the overall time complexity of merge sort is O(N\log{N})O(NlogN).

The space complexity of the merge sort algorithm is O(N)O(N), where {N}N is the length of the input list, since we need to keep the sublists as well as the buffer to hold the merge results at each round of merge process.



