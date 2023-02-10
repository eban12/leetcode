class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        res = []
        while i <= j:
            if nums[i] ** 2 >= nums[j] ** 2:
                res.append(nums[i]**2)
                i += 1
            else:
                res.append(nums[j]**2)
                j -= 1
        return res[::-1]
