class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        max_overlap = 0
        n = len(img1)
        for i in range(-n, n):
            for j in range(-n, n):
                temp = self.countOverlap(i, j, img1, img2)
                max_overlap = max(temp, max_overlap)
        return max_overlap
    
    def countOverlap(self, row, column, img1, img2):
        count = 0
        n = len(img1)
        for i in range(n):
            for j in range(n):
                if 0 <= i + row < n and 0 <= j + column < n and img1[i][j] == 1 and img1[i][j] == img2[i+row][j+column]:
                    count += 1
        return count
