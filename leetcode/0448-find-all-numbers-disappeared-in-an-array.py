##
#### Find All Numbers Disappeared in an Array (easy)
########################################################

# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not
# appear in nums.
 
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

# Constraints:
# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 
# Follow up: Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.

################################################################################


## subtract 2 sets
######################
class Solution:
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


## use hash map
###################
class Solution:
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        length, nums = len(nums) + 1, set(nums)

        return [x for x in range(1, length) if x not in nums]


## in place markers
#######################
class Solution:
    def find_disappeared_numbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            
            if nums[idx] > 0:
                nums[idx] *= -1

        result = []
        for j in range(1, len(nums) + 1):
            if nums[j - 1] > 0:
                result.append(j)

        return result
            
        #return [j for j in range(1, len(nums) + 1) if nums[j - 1] > 0]



## Tests
############

test1 = [4, 3, 2, 7, 8, 2, 3, 1]    #  [5,6]
test2 = [1, 1]                      # [2]

solution = Solution()
print(solution.find_disappeared_numbers(test1))
print(solution.find_disappeared_numbers(test2))

## LeetCode Solutions
#########################

## Approach 1: Using Hash Map
#################################
# time: O(n)
# space: O(n)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Hash table for keeping track of the numbers in the array
        # Note that we can also use a set here since we are not 
        # really concerned with the frequency of numbers.
        hash_table = {}
        
        # Add each of the numbers to the hash table
        for num in nums:
            hash_table[num] = 1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that don't appear in the hash table. 
        for num in range(1, len(nums) + 1):
            if num not in hash_table:
                result.append(num)
                
        return result


## Approach 2: O(1) Space InPlace Modification Solution
###########################################################
# time: O(n)
# space: O(1)
# 1. Iterate over the input array one element at a time.
# 2. For each element nums[i], mark the element at the corresponding location
#    negative if it's not already marked so
#    i.e. nums[nums[i] - 1] * -1
# 3. Now, loop over numbers from 1 ... N and for each number check
#    if nums[j] is negative. If it is negative, that means we've seen
#    this number somewhere in the array.
# 1. Add all the numbers to the resultant array which don't have their
#    corresponding locations marked as negative in the original array.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Iterate over each of the elements in the original array
        for i in range(len(nums)):
            
            # Treat the value as the new index
            new_index = abs(nums[i]) - 1
            
            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative 
            # thus indicating that the number nums[i] has 
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1
        
        # Response array that would contain the missing numbers
        result = []    
        
        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array 
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)
                
        return result

