# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        j = 0
        for i in range(n):
            nums[j] = nums[i]
            j += 1 if nums[i] else 0
        nums[j:] = [0] * (n - j)

        """
        Do not return anything, modify nums in-place instead.
        """
