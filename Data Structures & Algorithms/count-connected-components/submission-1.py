class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # represent the edges as a adjacency list
        aList = defaultdict(list)

        for x,y in edges:
            aList[x].append(y)
            aList[y].append(x)
        
        # connected component: a group of nodes compactly together distinct 
        visited=set()
        components = 0
        def dfs(node):
            visited.add(node)
            for nei in aList[node]:
                if nei not in visited:
                    dfs(nei)

        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1
        return components
        
        