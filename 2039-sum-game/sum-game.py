class Solution(object):
    def sumGame(self, num):
        n = len(num)
        mid = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        diff = left_sum - right_sum
        qdiff = right_q - left_q

        return 2 * diff != 9 * qdiff