class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])

        q=deque()

        # track rotten fruit in queue 
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        minutes = 0
        while q and fresh > 0:
            # retrieve earliest rotten fruit from queue
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc

                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1):
                        # we have fresh fruit remaining
                        q.append((nr,nc))
                        fresh -= 1
                        grid[nr][nc] = 2
            minutes += 1
        if fresh == 0:
            return minutes
    
        return -1