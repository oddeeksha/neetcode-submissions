class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        number_of_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1" and (row, col) not in visited:
                    stack = [(row, col)]
                    visited.add((row,col))                    
                    while stack:
                        curr_r, curr_c = stack.pop()
                        for r, c in [(curr_r, curr_c+1), (curr_r, curr_c-1), (curr_r+1, curr_c), (curr_r-1,curr_c) ]:
                            if r >=0 and r < len(grid) and c>=0 and c < len(grid[0]):
                                if grid[r][c] == "1" and (r,c) not in visited:
                                    stack.append((r,c))
                                    visited.add((r,c))
                    number_of_islands +=1   
        return number_of_islands            
                    


        
        
        