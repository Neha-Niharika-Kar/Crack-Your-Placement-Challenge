# ARRAYS - Easy

# Given an array of integers nums containing n + 1 integers, where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number without modifying the array.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
                
