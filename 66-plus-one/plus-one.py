class Solution(object):
    def plusOne(self, digits):
        dig = "".join(str(digit) for digit in digits)
        digit = str(int(dig) + 1)
        digits = [int(d) for d in digit]
        return digits

