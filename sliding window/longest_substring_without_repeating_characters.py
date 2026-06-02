# Problem: Longest Substring Without Repeating Characters
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use a sliding window with a hash set.
# Expand the window using the right pointer.
# If a duplicate character appears, shrink the window
# from the left until the duplicate is removed.

# Time Complexity: O(n)
# Space Complexity: O(min(n, m))
# m = size of character set

# Common Mistake:
# Forgetting to remove characters from the set
# while moving the left pointer.

# Revision Note:
# Fundamental Sliding Window problem.
# Important for understanding variable-size windows.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charSet = set()

        left = 0
        maxLength = 0

        for right in range(len(s)):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])

            maxLength = max(maxLength, right - left + 1)

        return maxLength