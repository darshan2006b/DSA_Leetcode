class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        r = 0
        longest = 0
        n = len(s)
        sett = set()

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            g = r - l + 1
            longest = max(longest,g)

        return longest