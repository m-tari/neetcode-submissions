# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        groupPrev = dummy  # The node just before this group

        while True:
            # Find the kth node
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Reverse the group
            groupNext = kth.next  # The node just after this group
            # This line is the key to making the reversal clean and safe. 
            # prev is initialized to groupNext so the reversed group will automatically point
            # to the node after the group (i.e., the next group's head).
            prev, curr = groupNext, groupPrev.next  
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Connect to the next group
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev =  tmp

# 1 2 3 -> 4 5 6 - > 7 8 9
                     
# 3 2 1 -> 6 5 4  -> 9 8 7
