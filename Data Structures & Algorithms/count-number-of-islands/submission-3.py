class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def inRange(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r,c):
            if not inRange(r,c) or grid[r][c] == "0":
                return
            
            if grid[r][c] == "1":
                grid[r][c] = "0"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    num_islands += 1
                    
        return num_islands
