# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find mid
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        # reverse the second half
        second = s.next
        s.next = None # separate the second list from first
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        