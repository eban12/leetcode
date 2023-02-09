class Solution:
    def maximumSwap(self, num: int) -> int:
        num_lst = list(str(num))
        i = 0
        swapped = False
        while not swapped and i < len(num_lst):
            b = i
            for j in range(i+1, len(num_lst)):
                if num_lst[j] >= num_lst[b]:
                    b = j
                    
            if b != i and num_lst[i] < num_lst[b]:
                num_lst[b], num_lst[i] = num_lst[i], num_lst[b]
                swapped = True
            i += 1
        return int("".join(num_lst))
