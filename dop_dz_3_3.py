class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True


test = Solution()
print(test.containsDuplicate([1, 1, 2, 3, 4, 5]))
print(test.containsDuplicate([1, 2, 3, 4, 5]))
