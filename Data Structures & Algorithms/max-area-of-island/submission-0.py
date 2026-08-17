class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        maxArea = 0
        visited = set()


        def bfs(r,c):
            q=deque()
            visited.add((r,c))
            q.append((r,c))

            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            curr = 1
            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    new_r,new_c = dr+r,dc+c

                    if (new_r in range(rows) and
                        new_c in range(cols) and
                        grid[new_r][new_c] == 1 and
                        (new_r,new_c) not in visited):
                        visited.add((new_r,new_c))
                        q.append((new_r,new_c))
                        curr += 1
            return curr

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea=max(maxArea,bfs(r,c))

        return maxArea