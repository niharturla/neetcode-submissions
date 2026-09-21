class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def search(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))


            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr=dr+r
                    nc=dc+c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    search(r,c)
                    num_islands += 1
                    
        return num_islands
