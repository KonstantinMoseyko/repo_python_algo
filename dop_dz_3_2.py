# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(ListNode):
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s


l1 = Solution()
l1.middleNode([1, 3, 4, 5, 6, 7])
