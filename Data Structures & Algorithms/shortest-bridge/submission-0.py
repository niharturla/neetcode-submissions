class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        min_flips = float('inf')
        m = len(grid)
        n = len(grid[0])
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        # convert first island to "A"
        def inRange(r,c):
            return 0 <= r < m and 0 <= c < n

        def spread(r,c):
            q = deque()
            q.append((r,c))

            while q:
                r,c = q.popleft()
                for dr,dc in d:
                    nr,nc = r+dr,c+dc
                    if inRange(nr,nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
        def bfs():
            q = deque()

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        q.append((i,j))
            dist = 0
            while q:
                
                for _ in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in d:
                        nr,nc=r+dr,c+dc
                        if inRange(nr,nc):
                            if grid[nr][nc] == 0:
                                grid[nr][nc] = 2
                                q.append((nr,nc))
                            elif grid[nr][nc] == 1:
                                return dist
                dist += 1
            return -1
                

        def convert():
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        spread(r,c)
                        return
        convert()
        return bfs()

        
        

        
        

