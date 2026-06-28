# Problem: Merge k Sorted Lists
# Platform: LeetCode
# Difficulty: Hard

# Approach:
# Merge the linked lists in pairs.
#
# In each round:
# - Merge list 1 with list 2.
# - Merge list 3 with list 4.
# - Continue until only one list remains.
#
# Pairwise merging reduces the number
# of lists by half each round.

# Time Complexity: O(N log k)
# N = Total number of nodes
# k = Number of linked lists

# Space Complexity: O(1)
# (Ignoring the temporary list used to store merged heads.)

# Common Mistake:
# Placing the remaining-node attachment
# and return statement inside the while loop.
# They must execute only after one list
# has been completely processed.

# Revision Note:
# Merge Sort Idea:
#
# k lists
# ↓
# Pairwise Merge
# ↓
# Pairwise Merge
# ↓
# One Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        if not lists:
            return None

        while len(lists) > 1:

            merged = []

            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(self.merge_lists(l1, l2))

            lists = merged

        return lists[0]

    def merge_lists(self, l1, l2):

        dummy = ListNode()
        tail = dummy

        while l1 and l2:

            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next