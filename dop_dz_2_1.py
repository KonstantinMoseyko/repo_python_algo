# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(s: List[str], i: int):
            if i >= len(s) // 2:
                return

            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
            helper(s, i + 1)

        helper(s, 0)