from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        components = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == "1":
                    queue = deque([(row,col)])
                    visited.add((row,col))
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        for r, c in [(curr_r, curr_c+1), (curr_r, curr_c-1), (curr_r-1, curr_c), (curr_r+1, curr_c)]:
                            if 0<=r<ROWS and 0<=c<COLS and grid[r][c] == "1"  and (r,c) not in visited :
                                queue.append((r,c))
                                visited.add((r,c))
                    components+=1
        return components
                    


                        
                        


