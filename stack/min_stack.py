# Problem: Min Stack
# Platform: LeetCode
# Difficulty: Medium

# Approach:
# Store each value along with the minimum value
# seen so far in the stack.
# This allows getMin() to run in O(1) time.

# Time Complexity:
# push()   -> O(1)
# pop()    -> O(1)
# top()    -> O(1)
# getMin() -> O(1)

# Space Complexity: O(n)

# Common Mistake:
# Storing only values in the stack.
# Then getMin() would require O(n) traversal.

# Revision Note:
# Important Stack design problem.
# Store [value, min_so_far] at each position.

class MinStack:

    def __init__(self):
        self.st = []

    def push(self, value: int) -> None:

        min_val = self.getMin()

        if min_val is None or min_val > value:
            min_val = value

        self.st.append([value, min_val])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None