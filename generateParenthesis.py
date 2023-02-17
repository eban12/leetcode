class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        comb = [0]*(2*n)
        ans = []
        self.helper(ans, comb, n, n, 0)
        return ans
    
    def helper(self, ans, comb, leftRemain, rightRemain, index):
        if leftRemain < 0 or rightRemain < leftRemain:
            return 
        
        if leftRemain == rightRemain == 0:
            ans.append(''.join(comb))
        else:
            comb[index] = '('
            self.helper(ans, comb, leftRemain-1, rightRemain, index+1)
            
            comb[index] = ')'
            self.helper(ans, comb, leftRemain, rightRemain-1, index+1)

        
