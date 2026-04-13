# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev, cur = dummy, head
        prev.next = cur

        for _ in range(1, left):
                cur = cur.next
                prev = prev.next
            
        leftNode = cur
        prevLeftNode = prev

        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        leftNode.next = cur
        prevLeftNode.next = prev

        return dummy.next

