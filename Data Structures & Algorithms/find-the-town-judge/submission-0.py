class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees=[0] * (n+1)
        outdegrees=[0] * (n+1)

        for a,b in trust:
            outdegrees[a] += 1
            indegrees[b] += 1
        
        for person in range(1,n+1):
            if outdegrees[person] == 0 and indegrees[person] == n - 1:
                return person
        return -1
        
            
