# ARRAYS - Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        
        right = 1
        for i in reversed(range(n)):
            answer[i] *= right
            right *= nums[i]
    
        return answer
