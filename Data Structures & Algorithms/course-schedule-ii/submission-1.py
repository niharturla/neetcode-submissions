class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList=defaultdict(list)
        for a,b in prerequisites:
            adjList[b].append(a)
        
        sort = []
        # we want the topological sort of the graph

        # build the indegrees
        indegree = [0] * numCourses
        for course in adjList:
            for nei in adjList[course]:
                indegree[nei] += 1
        
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            sort.append(course)
            for nei in adjList[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(sort) != numCourses:
            return []
        return sort

