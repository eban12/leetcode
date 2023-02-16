class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        
        counts = Counter(changed)
        changed.sort()
        original = []
        for i in range(n):
            if counts[changed[i]] != 0:
                double = changed[i] * 2
                if double not in counts or counts[double] == 0:
                    return []
                original.append(changed[i])
                counts[double] -= 1
                counts[changed[i]] -= 1
        return original
