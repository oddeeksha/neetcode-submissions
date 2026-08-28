from collections import deque
class Solution:
     
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647
        queue = deque()
        def bfs(x_cor, y_cor, dist):
            dist += 1
            for r, c in [(x_cor-1, y_cor), (x_cor+1, y_cor), (x_cor, y_cor+1), (x_cor, y_cor-1)]:
                if 0<=r<ROWS and 0<=c<COLS and grid[r][c] == INF :
                    grid[r][c] = dist
                    queue.append((r,c,dist))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c,0))
                    
        while queue:
            for cell in range(len(queue)):
                x_cor, y_cor, dist = queue.popleft()
                bfs(x_cor,y_cor, dist)
                

        