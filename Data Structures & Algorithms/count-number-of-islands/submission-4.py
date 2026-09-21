class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def inRange(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r,c):
            stack = []
            stack.append((r,c))

            while stack:
                r,c = stack.pop()
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if inRange(nr,nc) and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    num_islands += 1
                    
        return num_islands
