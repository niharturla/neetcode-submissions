class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res,sol=[],[]
        n = len(nums)

        # sort nums
        nums.sort()
        def bt(i):
            if i == n:
                if sol not in res:
                    res.append(sol[:])
                return

            bt(i+1) # not take it
            
            sol.append(nums[i]) # take it
            bt(i+1)
            sol.pop()
        bt(0)
        return res






        