# Problem: Binary Search
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use two pointers (left and right).
# Check the middle element.
# If target is smaller, search left half.
# If target is larger, search right half.

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Common Mistake:
# Using left < right instead of left <= right
# can miss the last remaining element.

# Revision Note:
# Fundamental Binary Search pattern.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1