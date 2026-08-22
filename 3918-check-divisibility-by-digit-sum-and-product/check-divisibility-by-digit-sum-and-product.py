class Solution(object):
    def checkDivisibility(self, n):
        original = n
        sum = 0
        prod = 1

        while n > 0:

            digit = n % 10

            sum += digit
            prod *= digit

            n //= 10
        
        return original % (sum + prod) == 0