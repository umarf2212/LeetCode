class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        curMin = prices[0]
        maxDiff = 0
        for price in prices:
            curMin = min(curMin, price)
            maxDiff = max(maxDiff, price-curMin)

        return maxDiff
