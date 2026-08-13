class Solution(object):
    def mostFrequentEven(self, nums):
        h = {}
        max_freq = 0
        answer = float('inf')

        for num in nums:
            if num % 2 == 0:
                h[num] = h.get(num,0) + 1

        if not h:
            return -1

        for num,count in h.items():
            if count > max_freq:
                max_freq = count
                answer = num
            elif max_freq == count:
                answer = min(answer,num)
        return answer