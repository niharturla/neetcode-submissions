class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # 1. prices[r] >= prices[l]
        # 2. have condition while r < len(prices)
        # 3. If we don't find greater price move left next because eventually we will 
        #.   either not find it or have a higher profit with next move

        left = 0
        maxprofit=0
        for right in range(1,len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                if profit >= maxprofit:
                    maxprofit = profit
        return maxprofit