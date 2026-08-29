class Solution(object):
    def isPalindrome(self, s):
        strr = []
        str = s.lower()
        strr = [(st) for st in str if st.isalnum()]
        str = "".join((st) for st in strr)
        n = len(str)
        left = 0
        right = n - 1

        while left <= right:
            if str[left] != str[right]:
                return False
            left += 1
            right -= 1

        return True