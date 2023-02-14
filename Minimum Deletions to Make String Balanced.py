class Solution:
    def minimumDeletions(self, s: str) -> int:
        aCount = s.count('a')
        bCount = 0
        ans = len(s)
        for c in s:
            if c == 'a':
                aCount -= 1
            
            ans = min(ans, aCount+bCount)
            
            if c == 'b':
                bCount += 1
        return ans
