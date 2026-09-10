class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Use Kahn's algorithm to find topological sort of the courses

        If length(ordering) < numCourses -> cycle detect and return []
        """

        adjList = defaultdict(list)

        for end,start in prerequisites:
            adjList[start].append(end)
        n=numCourses
        indegree = [0] * numCourses
        res = []
        q = deque()

        for i in range(n):
            for next_node in adjList[i]:
                indegree[next_node] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            for conn in adjList[node]:
                indegree[conn] -= 1
                if indegree[conn] == 0:
                    q.append(conn)
        if len(res) != numCourses:
            return []
        return res
        



        




        if len(q) < numCourses:
            return []