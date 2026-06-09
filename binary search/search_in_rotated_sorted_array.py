# Problem: Search in Rotated Sorted Array
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use Binary Search.
# At every step, one half of the array is guaranteed
# to be sorted.
#
# Check which half is sorted:
#
# Left Half Sorted:
# nums[left] <= nums[mid]
#
# Right Half Sorted:
# nums[mid] < nums[left]
#
# Determine whether the target lies inside the sorted half.
# If yes, search there.
# Otherwise search the other half.

# Time Complexity: O(log n)
# Space Complexity: O(1)

# Common Mistake:
# Returning nums[mid] instead of mid.
# The problem asks for the INDEX of the target,
# not the target value itself.

# Revision Note:
# In a rotated sorted array,
# one side is always sorted.
# Find the sorted side first,
# then decide where the target can exist.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[left]:

                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:

                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1