# SORTING AND SEARCHING - Medium

# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if len(nums) == 1:
                return i
            elif i == 0:
                if nums[i] > nums[i+1]:
                    return i
            elif i == len(nums)-1:
                if nums[i] > nums[i-1]:
                    return i
            else:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
