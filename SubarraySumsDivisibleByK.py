class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = defaultdict(int)
        prefix = 0
        count = 0
        for i in range(len(nums)):
            prefix += nums[i]
            modulo = prefix % k
            if modulo == 0:
                count += 1
            
            count += remainder[modulo]
            remainder[modulo] += 1
        return count
