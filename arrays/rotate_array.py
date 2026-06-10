# Problem: Rotate Array
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use the Reversal Algorithm.
#
# Example:
# nums = [1,2,3,4,5,6,7]
# k = 3
#
# Step 1: Reverse entire array
# [7,6,5,4,3,2,1]
#
# Step 2: Reverse first k elements
# [5,6,7,4,3,2,1]
#
# Step 3: Reverse remaining elements
# [5,6,7,1,2,3,4]
#
# Array rotated successfully.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting:
# k %= len(nums)
#
# Example:
# n = 7
# k = 10
#
# Rotation by 10 is same as rotation by 3.

# Revision Note:
# Reversal Algorithm:
# 1. Reverse whole array
# 2. Reverse first k elements
# 3. Reverse remaining elements

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k %= len(nums)

        def reverse(left, right):

            while left < right:

                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right -= 1

        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)