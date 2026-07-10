# Problem: Count Good Nodes in Binary Tree
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use Depth-First Search (DFS) while keeping track of the
# maximum value seen from the root to the current node.
#
# A node is considered "good" if its value is greater than
# or equal to every value encountered on the path from the
# root to that node.
#
# Steps:
# 1. Start DFS from the root.
# 2. Pass the maximum value seen so far.
# 3. If the current node's value is >= max_so_far,
#    count it as a good node.
# 4. Update max_so_far before visiting the children.
# 5. Return the total count from the left and right subtrees.

# Time Complexity: O(n)
# Space Complexity: O(h)
# h = Height of the tree (recursion stack)

# Common Mistake:
# Forgetting to update max_so_far before visiting
# the left and right children.

# Revision Note:
#
# DFS
# ↓
# Keep maximum value seen on the path
# ↓
# Current value >= maximum?
# ↓
# Count it as a good node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):

            if not node:
                return 0

            if node.val >= max_so_far:
                count = 1
            else:
                count = 0

            new_max = max(max_so_far, node.val)

            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)