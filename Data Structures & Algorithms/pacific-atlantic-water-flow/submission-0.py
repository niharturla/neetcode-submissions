class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac=set()
        atl=set()

        rows,cols = len(heights), len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def inRange(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c, visited):
            visited.add((r,c))
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if inRange(nr,nc) and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:
                    dfs(nr,nc,visited)
            
        for c in range(cols):
            dfs(0,c,pac)
        for r in range(rows):
            dfs(r,0,pac)
        
        for c in range(cols):
            dfs(rows-1,c,atl)
        for r in range(rows):
            dfs(r,cols-1,atl)

        res=[]

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res