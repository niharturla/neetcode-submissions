class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for a,b in prerequisites:
            adjList[b].append(a)
        
        # cycle detection with kahn's algorithm
        indegree = [0] * numCourses
        count = 0
        for course in adjList:
            for nei in adjList[course]:
                indegree[nei] += 1
        q = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        while q:

            course = q.popleft()
            count += 1

            for nei in adjList[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return count == numCourses

