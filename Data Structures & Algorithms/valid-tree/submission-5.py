class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """

        Can we assume graph is connected?

        Construct adj list with default dict

        run bfs on nodes if we encounter a cycle


        """

        if not edges:
            return True

        visited = set()
        q = deque()
        adjList = defaultdict(list)

        for (start, end) in edges:
            adjList[start].append(end)
            adjList[end].append(start)
        
        q.append(edges[0][0])
        visited.add(edges[0][0])


        while q:
            x = q.popleft()           
            for i in range(len(adjList[x])):
                if adjList[x][i] in visited:
                    return False
                visited.add(adjList[x][i])
                # cancel link in the adj list of y
                adjList[adjList[x][i]].remove(x)
                q.append(adjList[x][i])

        return len(visited) == n



