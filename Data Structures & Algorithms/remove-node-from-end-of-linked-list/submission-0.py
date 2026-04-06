# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        # length N
        N = 0
        cur = head
        while cur:
            cur = cur.next
            N += 1

        # Edge case - remove head
        removeIndex = N - n
        if removeIndex == 0:
            return head.next

        # remove removeIndex
        cur = head
        for i in range(removeIndex - 1):
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next
        
        return head
