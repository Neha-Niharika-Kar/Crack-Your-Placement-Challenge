# ARRAYS - Medium

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        op = 0
        n = len(nums)
        nums.sort()
        left, right = 0, n-1

        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                op += 1
                left += 1
                right -= 1
            elif total < k:
                left += 1
            else:
                right -= 1
                
        return op
