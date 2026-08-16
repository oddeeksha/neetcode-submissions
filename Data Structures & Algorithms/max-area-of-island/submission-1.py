from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row,col) not in visited:
                    area = 1
                    queue = deque([(row,col)])
                    visited.add((row,col))
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for r, c in [(curr_r-1, curr_c), (curr_r+1, curr_c), (curr_r,curr_c-1), (curr_r, curr_c+1)]:
                            if 0<=r<ROWS and 0<=c<COLS and (r,c) not in visited and grid[r][c] == 1:
                                queue.append((r,c))
                                visited.add((r,c))
                                area += 1
                    max_area = max(max_area, area)
        return max_area

        