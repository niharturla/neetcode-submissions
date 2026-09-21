class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        sol=[]

        def dfs(i, sol):
            if i >= len(nums):
                return
            if sum(sol) > target:
                return
            if sum(sol) == target:
                res.append(sol[:])
                return
            
            # take the current index
            sol.append(nums[i])
            dfs(i, sol)
            sol.pop()

            # move to next index
            dfs(i+1, sol)
        dfs(0,[])
        return res
             

