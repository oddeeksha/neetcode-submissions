class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        p_queue = collections.deque()
        p_visited = set()
        a_queue = collections.deque()
        a_visited = set()
        def bfs(r,c, queue, visited):
            for row, col in [(r-1,c), (r+1,c), (r, c-1), (r,c+1)]:
                if 0<=row < len(heights) and 0<=col<len(heights[0]) and heights[row][col] >= heights[r][c] and (row,col) not in visited:
                    queue.append((row,col))
                    visited.add((row,col))




        for i in range(len(heights[0])):
            p_queue.append((0,i))
            p_visited.add((0,i))
            a_queue.append((len(heights)-1, i))
            a_visited.add((len(heights)-1, i))
        for i in range(len(heights)):
            p_queue.append((i,0))
            p_visited.add((i,0))
            a_queue.append((i, len(heights[0])-1))
            a_visited.add((i, len(heights[0])-1))
        
        while p_queue:
            r, c = p_queue.popleft()
            bfs(r,c, p_queue,p_visited)
        while a_queue:
            r, c = a_queue.popleft()
            bfs(r,c, a_queue, a_visited)
        result = []
        for i in p_visited:
            if i in a_visited:
                result.append(i)
        return result

        



