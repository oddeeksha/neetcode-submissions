from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        def find_treasure():
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 0:
                        queue.append((row,col))
                       
        def add_cell(r,c,dist):
            if 0<=r<ROWS and 0<=c<COLS and grid[r][c] == INF:
                grid[r][c] = dist
                queue.append((r,c))
        find_treasure()
        dist = 1
        while queue:
            for i in range(len(queue)):
                curr_r, curr_c = queue.popleft()
                add_cell(curr_r, curr_c+1, dist)
                add_cell(curr_r, curr_c-1,dist)
                add_cell(curr_r+1, curr_c, dist)
                add_cell(curr_r-1, curr_c,dist)
            dist += 1
        
         


        