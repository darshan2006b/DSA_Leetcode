class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        n = len(s)

        return len(words[-1])