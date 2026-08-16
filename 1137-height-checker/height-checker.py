class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        num = 0

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                num += 1
        return num
        