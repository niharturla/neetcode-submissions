class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        
        for i in range(n-2,-1,-1):
            cost[i] = min(cost[i+1],cost[i+2]) + cost[i]
        return min(cost[0],cost[1])