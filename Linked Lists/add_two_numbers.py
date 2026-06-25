# Problem: Add Two Numbers
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Traverse both linked lists simultaneously.
#
# At each step:
# 1. Add values from both nodes (if present).
# 2. Add the carry from the previous addition.
# 3. Create a new node with digit = total % 10.
# 4. Update carry = total // 10.
#
# Continue until both lists are exhausted
# and there is no carry left.

# Time Complexity: O(max(n, m))
# n = length of l1
# m = length of l2

# Space Complexity: O(max(n, m))
# (Output linked list is not counted as extra space.)

# Common Mistake:
# Forgetting to process the final carry.
#
# Example:
# 9 -> 9
# 1
#
# Answer should be:
# 0 -> 0 -> 1

# Revision Note:
# Addition Pattern:
# total = carry + value1 + value2
#
# digit = total % 10
# carry = total // 10

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        res = dummy

        carry = 0

        while l1 or l2 or carry:

            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            digit = total % 10
            carry = total // 10

            dummy.next = ListNode(digit)
            dummy = dummy.next

        return res.next