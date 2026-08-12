class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        n = len(nums)
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        for num in nums:
            if freq[num] > (n/2):
                return num
