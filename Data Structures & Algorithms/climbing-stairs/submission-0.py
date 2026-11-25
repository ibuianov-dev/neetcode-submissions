class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        previous = 0
        current = 1

        for _ in range(n):
            previous, current = current, previous + current

        return current

