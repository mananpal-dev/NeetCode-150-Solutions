# Problem: Copy List with Random Pointer
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use a Hash Map to store the mapping between
# each original node and its copied node.
#
# Pass 1:
# Create a copy of every node.
#
# Pass 2:
# Connect the next and random pointers
# using the hash map.
#
# Finally, return the copied head.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting:
# hash = {None: None}
#
# This allows:
# copy.next = hash[cur.next]
# copy.random = hash[cur.random]
#
# to work even when next or random is None.

# Revision Note:
# Two Pass Algorithm:
#
# Pass 1 → Copy all nodes.
# Pass 2 → Connect next and random pointers.

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(
        self,
        head: 'Optional[Node]'
    ) -> 'Optional[Node]':

        node_map = {None: None}

        cur = head

        # Pass 1: Create copied nodes
        while cur:
            node_map[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        # Pass 2: Connect next and random pointers
        while cur:

            copy = node_map[cur]

            copy.next = node_map[cur.next]
            copy.random = node_map[cur.random]

            cur = cur.next

        return node_map[head]