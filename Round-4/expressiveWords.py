class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def count(S):
            return zip(*[(k, len(list(grp))) for k, grp in itertools.groupby(S)])

        chars1, counts1 = count(s)
        ans = 0
        for word in words:
            chars2, counts2 = count(word)

            if chars1 != chars2: continue

            ans += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(counts1, counts2))

        return ans
