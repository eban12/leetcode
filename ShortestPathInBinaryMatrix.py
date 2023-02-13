class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque([])
        visited = set()
        if grid[0][0] == 0:
            queue.append((0, 0, 1))
            visited.add((0,0))

        while queue:
            i, j, d = queue.popleft()
            if i == len(grid)-1 and j == len(grid)-1: return d
            for k, l in [(i+1, j), (i-1, j), (i+1, j+1), (i-1, j-1), (i, j+1), (i, j-1), (i-1, j+1), (i+1, j-1)]:
                if 0 <= k < len(grid) and 0 <= l < len(grid[0]) and grid[k][l] == 0 and (k, l) not in visited:
                    visited.add((k,l))
                    if k == len(grid)-1 and l == len(grid)-1: return d+1
                    queue.append((k, l, d+1))
        return -1
      
