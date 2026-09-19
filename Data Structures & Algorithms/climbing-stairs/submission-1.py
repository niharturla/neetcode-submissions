class Solution:
    memo={}
    def climbStairs(self, n: int) -> int:
        if n in self.memo.keys():
            return self.memo[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = res
        return res