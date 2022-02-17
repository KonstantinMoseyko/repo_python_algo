# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last = nums[0]
        j = 1

        for i in range(1, len(nums)):
            if nums[i] != last:
                nums[j] = nums[i]
                last = nums[i]
                j += 1

        return j
