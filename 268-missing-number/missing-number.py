class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        summ = sum(nums)
        total = n * (n + 1) // 2

        return total - summ
        