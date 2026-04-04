class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        window = set()
        l = r = 0
        maxV = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r]- prices[l]
                maxV = max(profit, maxV)
            else:
                l=r
            r+=1
            
        return maxV