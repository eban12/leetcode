class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = list(range(n-1))
        ans.append(-sum(ans))
        return ans
        
