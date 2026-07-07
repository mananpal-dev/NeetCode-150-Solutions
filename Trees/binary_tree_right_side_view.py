# Problem: Binary Tree Right Side View
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use Breadth-First Search (BFS) with a Queue.
#
# Process the tree level by level.
# For each level:
# 1. Traverse all nodes in that level.
# 2. Keep updating the current rightmost node.
# 3. After the level is complete, add the last
#    node's value to the result.
#
# Since nodes are processed from left to right,
# the last node visited at each level is the
# rightmost node.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting to check if a node is None before
# accessing its children. Since None values are
# added to the queue, always verify the node exists.

# Revision Note:
#
# BFS
# ↓
# Process one level
# ↓
# Last node of the level
# ↓
# Add to answer

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        queue = deque([root])

        while queue:

            rightmost = None

            for _ in range(len(queue)):

                node = queue.popleft()

                if node:
                    rightmost = node

                    queue.append(node.left)
                    queue.append(node.right)

            if rightmost:
                result.append(rightmost.val)

        return result