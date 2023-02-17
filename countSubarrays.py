class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        subArrays = 0
        l = 0
        r = 0
        lastMinK = -1
        lastMaxK = -1
        while r < len(nums):
            if nums[r] < minK or nums[r] > maxK:
                r += 1
                l = r
                lastMinK = -1
                lastMaxK = -1
                continue

            if nums[r] == minK:
                lastMinK = r
            
            if nums[r] == maxK:
                lastMaxK = r
            
            r += 1
            if lastMinK != -1 and lastMaxK != -1:
                subArrays += (min(lastMinK, lastMaxK) - l + 1)
        return subArrays
            
                
