# Problem: Permutation in String
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Use a fixed-size sliding window equal to len(s1).
# Track character frequencies for s1 and the current
# window in s2. If the frequency maps match,
# a permutation exists.

# Time Complexity: O(n)
# Space Complexity: O(1)

# Common Mistake:
# Forgetting to remove characters whose frequency
# becomes zero after sliding the window.

# Revision Note:
# Fixed-Size Sliding Window pattern.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = 1 + s1_count.get(s1[i], 0)
            s2_count[s2[i]] = 1 + s2_count.get(s2[i], 0)

        if s1_count == s2_count:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            s2_count[s2[right]] = 1 + s2_count.get(s2[right], 0)

            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]

            left += 1

            if s1_count == s2_count:
                return True

        return False