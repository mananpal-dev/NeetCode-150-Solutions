# Problem: LRU Cache
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Combine a Hash Map and a Doubly Linked List.
#
# Hash Map:
# Stores key -> node mapping for O(1) lookup.
#
# Doubly Linked List:
# Maintains the order of usage.
#
# Most Recently Used (MRU):
# Immediately after the head.
#
# Least Recently Used (LRU):
# Immediately before the tail.
#
# Operations:
#
# get(key):
# - Return value if key exists.
# - Move the node to the front (MRU).
#
# put(key, value):
# - If key exists, remove its old node.
# - Insert the new node at the front.
# - If capacity is exceeded,
#   remove the LRU node.

# Time Complexity:
# get() -> O(1)
# put() -> O(1)

# Space Complexity:
# O(capacity)

# Common Mistake:
# Updating the value without moving the node
# to the front.
#
# Every access makes the node the
# Most Recently Used (MRU).

# Revision Note:
# Hash Map + Doubly Linked List
#
# Head <-> MRU ... LRU <-> Tail

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):

        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):

        prev = self.head
        nxt = self.head.next

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:

            lru = self.tail.prev

            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)