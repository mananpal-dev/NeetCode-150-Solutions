# Problem: Trapping Rain Water
# Platform: LeetCode
# Difficulty: Hard

# Approach:
# Use two pointers and track the maximum height seen
# from both left and right sides.
# Water trapped at a position depends on the smaller
# boundary among left_max and right_max.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Using height[left] and height[right] for decisions
# instead of maintaining left_max and right_max properly.

# Revision Note:
# Advanced Two Pointers problem.
# Builds on the same intuition as Container With Most Water.

class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        water = 0

        while left < right:

            if height[left] < height[right]:

                left += 1

                left_max = max(left_max, height[left])

                water += left_max - height[left]

            else:

                right -= 1

                right_max = max(right_max, height[right])

                water += right_max - height[right]

        return water