# ARRAYS - Easy

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])

        return False
