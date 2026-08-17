class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # form the adjacency list
        adj_list=defaultdict(list)

        for end, start in prerequisites:
            adj_list[start].append(end)
        
        
        def topoSort(adj_list):
            
            # track the in-degree count
            indegree = [0] * numCourses
            res=[]
            q=deque()

            for node in adj_list:
                for next_node in adj_list[node]:
                    indegree[next_node] += 1
            
            # find all nodes with indegree 0
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
            
            while q:
                node = q.popleft()
                res.append(node)
                for conn in adj_list[node]:
                    indegree[conn] -= 1
                    if indegree[conn] == 0: # checks for cycle basically if there are no indegree of 0 then skip
                        q.append(conn)
            return len(res)
        return topoSort(adj_list) == numCourses
            





        
        