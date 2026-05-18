class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.size = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node) -> None:
        prev_n, next_n = node.prev, node.next
        prev_n.next, next_n.prev = next_n, prev_n
        del self.hashmap[node.key]

    def _insert(self, node) -> None:
        prev_n, next_n = self.tail.prev, self.tail
        prev_n.next = next_n.prev = node
        node.prev, node.next = prev_n, next_n
        self.hashmap[node.key] = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        new_node = Node(key, node.val)
        self._remove(node) # remove old node
        self._insert(new_node) # insert new node
        return new_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap: # remove old node if existed
            node = self.hashmap[key]
            self._remove(node)

        elif len(self.hashmap) == self.size: # remove old node if size full
            self._remove(self.head.next)

        new_node = Node(key, value)
        self._insert(new_node) # insert new node
