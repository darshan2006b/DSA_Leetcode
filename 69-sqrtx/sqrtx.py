class Solution(object):
    def mySqrt(self, x):
        L ,R = 1 ,x

        while L <= R:
            M = (L + R) // 2
            M_squared = M * M

            if M_squared <= x:
                L = M + 1
            else:
                R = M - 1
        return R