class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = Counter(nums)
        pairs = 0
        for num in nums:
            if target.startswith(num):
                suffix = target[len(num):]
                
                if suffix in count:
                    pairs += count[suffix]
                    if num == suffix:
                        pairs -= 1

        return pairs
