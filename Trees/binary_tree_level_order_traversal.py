# Problem: Binary Tree Level Order Traversal
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use Breadth-First Search (BFS) with a Queue.
#
# 1. Start by adding the root node to the queue.
# 2. Process one level at a time.
# 3. Before processing a level, store the current
#    queue size because it equals the number of
#    nodes in that level.
# 4. Remove each node, save its value, and add
#    its left and right children to the queue.
# 5. After finishing the level, add it to the result.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Iterating directly over the queue while adding
# new nodes. Always store the current queue size
# first, otherwise nodes from the next level
# will also be processed.

# Revision Note:
#
# Queue = Next nodes to visit
#
# While queue is not empty:
#     Process one complete level
#     Add children for next level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        if not root:
            return result

        queue = deque([root])

        while queue:

            level = []

            for _ in range(len(queue)):

                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result