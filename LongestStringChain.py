class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_predecessor(word_a, word_b):
            if (len(word_b) - len(word_a) != 1):
                return False

            diff_count = 0
            i = 0
            j = 0
            while i < len(word_a) and j < len(word_b):
                if word_a[i] != word_b[j]:
                    diff_count += 1
                else:
                    i += 1
                j += 1
            return diff_count <= 1

        chains = [1] * len(words)
        words.sort(key=len)
        for i in range(1, len(words)):
            for j in range(0, i):
                if is_predecessor(words[j], words[i]) and chains[i] < chains[j] + 1:
                    chains[i] = chains[j] + 1
        return max(chains)
