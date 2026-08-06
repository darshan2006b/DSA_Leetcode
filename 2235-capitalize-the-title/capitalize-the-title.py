class Solution(object):
    def capitalizeTitle(self, title):
        words = title.split()
        title1 = []
        for word in words:
            n = len(word)
            if n < 3:
                word2 = word.lower()
                title2 = title1.append(word2)
            else:
                word1 = word.lower()
                word2 = word.capitalize()
                title1.append(word2)
        return " ".join(title1)
