class Solution(object):
    def firstUniqChar(self, s):
        hash = {}

        for c in s:
            hash[c] = hash.get(c,0) + 1

        for  i,c in enumerate(s):
            if hash[c] == 1:
                return i

        return -1
        