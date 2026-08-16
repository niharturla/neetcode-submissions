class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # base case: stop when target-sum(sol) doesn't exist in array
        res,sol=[],[]
        nums.sort()
        n = len(nums)
        def backtrack(start, running):
            if running == 0:
                res.append(sol[:])
                return
            
            # for every number in nums up to running
            for i in range(start, n):
                if running < nums[i]:
                    break
                sol.append(nums[i])
                backtrack(i, running-nums[i]) # we can choose nums[i] any number of times
                sol.pop()
        backtrack(0,target)
        return res


                


