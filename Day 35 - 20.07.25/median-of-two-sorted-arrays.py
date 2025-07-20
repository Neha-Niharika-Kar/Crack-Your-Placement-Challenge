# ARRAYS - Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n % 2 != 0:
            return float(nums[n//2])
        else:
            return (nums[n//2 - 1] + nums[n//2]) / 2.0

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = total_left - i

            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]
            
            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                else:
                    return float(max(maxLeft1, maxLeft2))
            elif maxLeft1 > minRight2:
                right = i - 1
            else:
                left = i + 1
