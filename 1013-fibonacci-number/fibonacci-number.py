class Solution(object):
    def fib(self, n):
        memo = {0:0,1:1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                return f(x-1) + f(x-2)

        return f(n)