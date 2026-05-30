# Problem: Valid Palindrome
# Platform: LeetCode
# Difficulty: Easy

# Approach 1:
# Clean the string by keeping only alphanumeric
# characters and converting to lowercase.
# Use two pointers to compare characters.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting to ignore spaces, punctuation,
# and letter casing.

# Revision Note:
# Important Two Pointers pattern.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True


# --------------------------------------------------


# Approach 2:
# Clean the string and compare it with its reverse.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Forgetting that slicing creates a new string,
# increasing space usage.

# Revision Note:
# Short and Pythonic solution.

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())

        return s == s[::-1]