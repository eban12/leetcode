class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return -2**32
        
        sums = []
        
        def maxSub(nums):
            if nums[0] > 0:
                sums.append(nums[0])
            else:
                sums.append(0)

            for i in range(1,len(nums)):
                if sums[i-1] + nums[i] > 0:
                    sums.append(sums[i-1] + nums[i])
                else:
                    sums.append(0)

            if sum(sums) == 0:
                ans = nums[0]
                for i in nums:
                    if i > ans:
                        ans = i
                return ans
            
            ans = sums[0]
            for i in sums:
                if i > ans:
                    ans = i
            return ans
        return maxSub(nums)

