class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if we see that an element is smaller than current element we are going to move it as current since the difference will never decrease
        l = 0
        r = l + 1

        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit=max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit