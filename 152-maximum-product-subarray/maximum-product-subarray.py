class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        new_max = nums[0]
        new_min = nums[0]
        answer = nums[0]
        
        for i in range(1,n):
            old_max = new_max
            old_min = new_min

            new_max = max(nums[i],old_max * nums[i],old_min* nums[i])

            new_min = min(nums[i],old_max * nums[i],old_min* nums[i])

            answer = max(answer,new_max)
        return answer
