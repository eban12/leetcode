class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        latest_min = nums[0]
        ans = -1
        for num in nums:
            if num < latest_min:
                latest_min = num
            elif num > latest_min:
                ans = max(ans, num - latest_min)
        return ans
