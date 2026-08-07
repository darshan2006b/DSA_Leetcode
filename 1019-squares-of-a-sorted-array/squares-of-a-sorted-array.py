class Solution(object):
    def sortedSquares(self, nums):
        L = 0
        R = len(nums) - 1
        result = []
        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                result.append(nums[L] ** 2)
                L += 1
            else:
                result.append(nums[R] ** 2)
                R -= 1
        result.reverse()
        return result