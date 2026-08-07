class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for c in stones:
            if c in jewels:
                count += 1
            
        return count