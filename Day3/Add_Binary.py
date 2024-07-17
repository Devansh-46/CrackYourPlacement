class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, carry, res, = 0, 0, ''
        while i < len(a) or i < len(b) or carry:
            bi1 = int(b[-i-1]) if i < len(b) else 0
            bi2 = int(a[-i-1]) if i < len(a) else 0
            num = bi1 + bi2 + carry
            res = str(num%2) + res
            carry = 1 if num > 1 else 0
            i += 1
        return res