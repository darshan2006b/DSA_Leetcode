class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 1
        cur = 2

        for i in range(2,n):
            prev,cur = cur,prev + cur
        return cur
        