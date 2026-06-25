# Problem: Find the Duplicate Number
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Treat the array like a linked list.
#
# Index     -> Current Node
# nums[i]   -> Next Node
#
# Since one number is duplicated,
# two nodes point to the same node,
# creating a cycle.
#
# Use Floyd's Cycle Detection Algorithm:
#
# Phase 1:
# Find the meeting point of slow and fast pointers.
#
# Phase 2:
# Move one pointer to the beginning.
# Move both one step at a time.
# The node where they meet is the duplicate number.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Thinking the meeting point is the answer.
# The meeting point is inside the cycle,
# not necessarily at the start of the cycle.
# A second phase is required.

# Revision Note:
# Array → Linked List
#
# index = current node
# nums[index] = next node
#
# Duplicate → Cycle

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find intersection point
        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find cycle entrance
        slow2 = nums[0]

        while slow != slow2:

            slow = nums[slow]
            slow2 = nums[slow2]

        return slow