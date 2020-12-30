class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) in [0,1]: return 0        
        
        max_diff = 0
        min_elem = prices[0]
        
        for i in range(1, len(prices)):
            
            if prices[i] < min_elem:
                min_elem = prices[i]
                
            if prices[i] - min_elem > max_diff:
                max_diff = prices[i] - min_elem
                
        
        return max_diff
