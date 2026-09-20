class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max amount of money from first i houses
        """
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            # we can either rob the house or leave it and take the max 
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[len(nums)-1]

            