class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows = len(board)
        cols = len(board[0])
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr = dr+row
                    nc = dc+col
                    if inRange(nr,nc) and board[nr][nc] == "O":
                        # convert the O to a T
                        board[nr][nc] = "T"
                        q.append((nr,nc))


        def isEdge(r,c):
            return r == rows-1 or r == 0 or c == cols-1 or c == 0
        def inRange(r,c):
            return 0 <= r < rows and 0 <= c < cols
        
        for r in range(rows):
            for c in range(cols):
                if isEdge(r,c) and board[r][c] == "O":
                    board[r][c] = "T"
                    bfs(r,c)

        # convert all O to X

        # if there are O still on the board that means they don't reach to an edge
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
            
        
        
        