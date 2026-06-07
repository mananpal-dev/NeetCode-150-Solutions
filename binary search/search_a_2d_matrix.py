# Problem: Search a 2D Matrix
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# First use binary search to locate the correct row.
# Then perform binary search within that row.
# The matrix properties allow us to eliminate half
# the search space at each step.

# Time Complexity: O(log(m) + log(n))
# Space Complexity: O(1)

# Common Mistake:
# Using left < right instead of left <= right,
# which can skip checking the final element.

# Revision Note:
# Binary Search on rows + Binary Search on columns.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:

            row = (top + bot) // 2

            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bot = row - 1

            else:
                break

        if not (top <= bot):
            return False

        row = (top + bot) // 2

        left = 0
        right = cols - 1

        while left <= right:

            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True

            elif matrix[row][mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False