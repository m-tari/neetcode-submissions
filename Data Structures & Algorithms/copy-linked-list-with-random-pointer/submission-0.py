"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        mp = {None: None}

        cur = head
        while cur:
            node = Node(x=cur.val)
            mp[cur] = node
            cur = cur.next

        cur = head
        while cur:
            node = mp[cur]
            node.random = mp[cur.random]
            node.next = mp[cur.next]
            cur = cur.next


        return mp[head]
