class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        # 1 5 9
        
        # 32 35 36
        
        # 32 35 36
        
        # (32 // 10) * 10 = 30 = p'
        
        # p = 32
        # x = p % 10
        # p'' = p + (10-x) = 40
        
        x = purchaseAmount % 10
        
        if x == 5:
            return 100 - (purchaseAmount + 5)
        
        p_min = (purchaseAmount // 10) * 10
        p_max = purchaseAmount + (10 - x)
        
        if x < 5:
            return 100 - p_min
        else:
            return 100 - p_max
        
        