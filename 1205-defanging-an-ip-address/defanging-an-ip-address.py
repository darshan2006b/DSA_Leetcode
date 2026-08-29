class Solution(object):
    def defangIPaddr(self, address):
        add = address.replace(".","[.]")
        return add