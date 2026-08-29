class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        visited = set()
        result = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in visited:
                    result.append(grid[i][j])
                else:
                    visited.add(grid[i][j])
        
        no_of_elements = len(grid) * len(grid)
        total_sum = no_of_elements*(no_of_elements+1) //2
        missing_number = total_sum - sum(visited)
        result.append(missing_number)
        return result


             