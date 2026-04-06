# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        
        mid_point = len(lists) // 2
        l_list = lists[:mid_point]
        r_list = lists[mid_point:]

        l_merged = self.mergeKLists(l_list)
        r_merged = self.mergeKLists(r_list)

        merged_list = self.merge(l_merged, r_merged)

        return merged_list

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next





        