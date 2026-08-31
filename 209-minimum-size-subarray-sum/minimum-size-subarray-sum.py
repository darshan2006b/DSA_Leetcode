class Solution(object):
    def minSubArrayLen(self, target, nums):
        tar = 0
        left = 0
        lenght = 0
        min_len = float('inf')

        for right in range(len(nums)):
            tar += nums[right]
            while target <= tar:
                lenght = right - left + 1
                min_len = min(min_len,lenght)
            
                tar -= nums[left]
                left += 1
            
            
        if min_len == float('inf'):
            return 0

        return min_len