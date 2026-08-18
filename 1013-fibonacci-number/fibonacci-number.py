class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n+1)

        prev = 0
        cur = 1

        for i in range(2,n+1):
            prev,cur = cur,prev + cur
            
        return cur