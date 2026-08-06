class Solution(object):
    def detectCapitalUse(self, word):
        n = len(word)

        
        if word[0].isupper() and word[1:n].islower():
            return True
        elif word[0:n].isupper():
            return True
        elif word[0:n].islower():
            return True
        else:
            return False