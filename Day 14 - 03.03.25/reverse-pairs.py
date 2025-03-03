# ARRAYS - Medium

# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where:
#     0 <= i < j < nums.length and
#     nums[i] > 2 * nums[j].

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)

            # Count reverse pairs
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))

            # Merge step
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= right:
                temp.append(nums[j])
                j += 1

            nums[left:right + 1] = temp  # Copy sorted elements back
            return count

        return merge_sort(0, len(nums) - 1)
