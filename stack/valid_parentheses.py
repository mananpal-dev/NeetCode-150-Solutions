# Problem: Valid Parentheses
# Platform: LeetCode
# Difficulty: Easy

# Approach:
# Use a stack to keep track of opening brackets.
# When a closing bracket appears, check whether
# it matches the most recent opening bracket.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Common Mistake:
# Using stack.pop instead of stack.pop()
# returns the method object instead of the top value.

# Revision Note:
# Fundamental Stack problem.
# LIFO (Last In, First Out) pattern.

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:

            if char in mapping.values():
                stack.append(char)

            elif char in mapping.keys():

                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack