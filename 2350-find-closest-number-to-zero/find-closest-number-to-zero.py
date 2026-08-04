class Solution(object):
    def findClosestNumber(self, nums):
        close = nums[0]
        for x in nums:
            if abs(x) < abs(close):
                close = x
        
        if close < 0 and abs(close) in nums:
            return abs(close)
        else:
            return close