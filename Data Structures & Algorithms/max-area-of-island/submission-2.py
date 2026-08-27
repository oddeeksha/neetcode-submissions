from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        visited= set()
        def bfs(i,j):
            size = 0
            queue = deque([(i,j)])
            while queue:
                row, col = queue.popleft()
                size += 1
                for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                    if 0<=r<ROWS and 0<=c<COLS and grid[r][c] == 1 and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))
            return size

        for i in range(ROWS):
            for j in range(COLS):
                if  grid[i][j] == 1 and (i,j) not in visited :
                    visited.add((i,j))
                    max_area = max(max_area, bfs(i,j))
        return max_area

        


        