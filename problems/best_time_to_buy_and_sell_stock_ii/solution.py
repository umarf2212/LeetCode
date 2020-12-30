class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_stock = 0
        curr_diff = 0
        curr_min = prices[0]
        
        
        for i in range(1, len(prices)):
            
            if prices[i] < prices[i-1]:
                curr_min = prices[i]
                max_stock += curr_diff
                curr_diff = 0
            
            elif prices[i] - curr_min > curr_diff:
                curr_diff = prices[i] - curr_min
                
        if curr_diff > 0:
            max_stock += curr_diff
            
        return max_stock