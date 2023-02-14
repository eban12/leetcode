class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def check(num):
            num = str(num)
            num = sorted(num)
            num = ''.join(num)
            return num
        n = check(n)
        for i in range(31):
            if n == check(2**i):
                return True
        return False
