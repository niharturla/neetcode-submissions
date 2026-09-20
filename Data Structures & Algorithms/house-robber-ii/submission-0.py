class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        
        def rob_part(houses) -> int:
            n = len(houses)
            prev2 = 0
            prev1 = 0

            for i in range(n):
                curr = max(prev1, prev2 + houses[i])
                prev2=prev1
                prev1=curr
            return prev1
        res1=rob_part(nums[:len(nums)-1])
        res2=rob_part(nums[1:])
        return max(res1,res2)
