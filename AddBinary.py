class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def addBits(bit1, bit2):
            if bit1 == bit2 == 1:
                return 0, 1
            elif bit1 == 1 or bit2 == 1:
                return 1, 0
            else:
                return 0, 0
              
        a = a[::-1]
        b = b[::-1]
        ans = []
        n = len(a) if len(a) >= len(b) else len(b)
        carry = 0
        for i in range(n):
            bit1 = int(a[i]) if i < len(a) else 0
            bit2 = int(b[i]) if i < len(b) else 0
            val, temp = addBits(bit1, carry)
            val, temp2 = addBits(val, bit2)
            ans.append(str(val))
            carry = temp | temp2
        
        if carry:
            ans.append(str(carry))

        return "".join(ans[::-1])
