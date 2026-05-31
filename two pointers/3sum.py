# Problem: 3Sum
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Sort the array and fix one element.
# Use two pointers to find the remaining two numbers.
# Skip duplicates to avoid repeated triplets.

# Time Complexity: O(n²)
# Space Complexity: O(1) (excluding output array)

# Common Mistake:
# Moving pointers in the wrong direction.
# If sum is too small -> move left pointer right.
# If sum is too large -> move right pointer left.

# Revision Note:
# One of the most important Two Pointers problems.
# Builds directly on Two Sum II.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:

                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1

                else:

                    res.append([nums[i], nums[j], nums[k]])

                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return res