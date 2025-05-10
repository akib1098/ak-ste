class Solution:
    def fib(self, n):
        a, b = 0, 1
        if n == 0:
            return 0
        for i in range(n):
            c = a+b
            a, b = c, a
        return c

print(Solution().fib(3))