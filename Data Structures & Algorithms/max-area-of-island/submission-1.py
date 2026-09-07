class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            score = 1
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if (nr in range(rows) and 
                        nc in range(cols) and 
                        (nr,nc) not in visited and
                        grid[nr][nc] == 1):
                        score += 1
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return score
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    area=bfs(row,col)
                    max_area=max(area, max_area)
        return max_area
