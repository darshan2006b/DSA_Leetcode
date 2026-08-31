class Solution(object):
    def findMaxAverage(self, nums, k):
        number = 0
        for i in range(k):
            number += nums[i]
        max_num = number

        for i in range(k ,len(nums)):
            number += nums[i]
            number -= nums[i - k]

            max_num = max(max_num ,number)

        return float(max_num) / k
        