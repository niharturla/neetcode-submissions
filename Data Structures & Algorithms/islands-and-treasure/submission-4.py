class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows=len(grid)
        cols=len(grid[0])
        
        q=deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                new_r,new_c = r+dr,c+dc
                if (0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == INF):
                    grid[new_r][new_c] = grid[r][c] + 1
                    q.append((new_r,new_c))
        