# Problem: Reorder List
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# The solution consists of three steps:
#
# 1. Find the middle of the linked list using
#    slow and fast pointers.
#
# 2. Reverse the second half of the list.
#
# 3. Merge the first half and the reversed
#    second half alternately.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting:
# slow.next = None
#
# This separates the two halves.
# Without it, a cycle may be created during merging.

# Revision Note:
# Three-Step Pattern:
#
# 1. Find Middle
# 2. Reverse Second Half
# 3. Merge Alternately

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Step 1: Find Middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse Second Half
        second = slow.next
        slow.next = None

        node = None

        while second:
            temp = second.next
            second.next = node
            node = second
            second = temp

        # Step 3: Merge Both Halves
        first = head
        second = node

        while second:

            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2