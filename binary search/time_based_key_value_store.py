# Problem: Time Based Key-Value Store
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Store all values for a key along with their timestamps.
#
# set():
# Append (timestamp, value) to the list for that key.
#
# get():
# Use Binary Search to find the largest timestamp
# less than or equal to the requested timestamp.

# Time Complexity:
# set() -> O(1)
# get() -> O(log n)

# Space Complexity: O(n)

# Common Mistake:
# Returning only when timestamp matches exactly.
# The problem asks for the most recent value
# whose timestamp <= requested timestamp.

# Revision Note:
# Binary Search for:
# "largest valid timestamp <= target timestamp"

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""

        arr = self.store[key]

        left = 0
        right = len(arr) - 1

        res = ""

        while left <= right:

            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:

                res = arr[mid][1]
                left = mid + 1

            else:

                right = mid - 1

        return res