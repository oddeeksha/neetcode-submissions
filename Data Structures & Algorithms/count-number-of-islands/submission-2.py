from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            queue = deque([(i,j)])
            while queue:
                i, j = queue.popleft()
                for row, col in [(i-1, j), (i+1, j), (i, j-1), (i,j+1)]:
                    if 0<=row<len(grid) and 0<=col<len(grid[0]) and (row,col) not in visited and grid[row][col] == "1":
                        queue.append((row,col))
                        visited.add((row,col))

        count = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    bfs(i, j)
                    count += 1
        return count
        



    