from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        queue = deque()
        for i in range(COLS):
            if board[0][i] == "O" and (0,i) not in visited:
                queue.append((0,i))
                visited.add((0,i))
            if board[ROWS-1][i] == "O" and (ROWS-1,i) not in visited:
                queue.append((ROWS-1,i))
                visited.add((ROWS-1,i))
        for i in range(ROWS):
            if board[i][0] == "O" and (i,0) not in visited:
                queue.append((i,0))
                visited.add((i,0))
            if board[i][COLS-1] == "O" and (i,COLS-1) not in visited:
                queue.append((i,COLS-1))
                visited.add((i,COLS-1))
        while queue:
            r, c = queue.popleft()
            for row, col in [(r-1,c), (r+1,c), (r,c-1), (r, c+1)]:
                if 0<=row<ROWS and 0<=col<COLS and board[row][col]== "O" and (row,col) not in visited:
                    queue.append((row,col))
                    visited.add((row,col))
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row,col) not in visited:
                    board[row][col] = "X"
        


