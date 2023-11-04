# PROMPT

# You are climbing a staircase.
# It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

# PROMPT

# Solution


class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        return self.fib(n + 1)

    def fib(self, n):
        if n in self.cache:
            return self.cache[n]

        if n == 0 or n == 1:
            return n
        else:
            self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
            return self.cache[n]
