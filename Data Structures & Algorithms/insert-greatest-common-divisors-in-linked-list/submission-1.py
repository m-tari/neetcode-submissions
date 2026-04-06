# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        while cur and cur.next:
            val1 = cur.val
            val2 = cur.next.val
            tmp = cur.next

            gcd = self.getGcd(val1, val2)
            cur.next = ListNode(gcd, tmp)
            cur = tmp

        return head

    def getGcd(self, a, b):
        while b:
            a, b = b, a % b
        return a