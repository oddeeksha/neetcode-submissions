from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row,col))
        def add(r, c):
            if 0<=r<ROWS and 0<=c < COLS and grid[r][c] == 1:
                grid[r][c] = 2
                queue.append((r,c))
        minutes = 0
        while queue:
            for i in range(len(queue)):
                current_r, current_c = queue.popleft()
                add(current_r, current_c+1)
                add(current_r, current_c-1)
                add(current_r-1, current_c)
                add(current_r+1, current_c)
            minutes+=1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        return minutes-1 if minutes != 0 else 0


        