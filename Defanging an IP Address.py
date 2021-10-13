class Solution:
    def defangIPaddr(self, address: str) -> str:
        new = ""
        for i in address:
            if i != '.':
                new += i
            else:
                new += '['
                new += i
                new += ']'
        return new