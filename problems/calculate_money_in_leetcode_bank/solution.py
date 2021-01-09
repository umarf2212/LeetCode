class Solution:
    def totalMoney(self, n: int) -> int:
        
        weeks = n // 7
        days = n % 7
        savings = 0
        
        week = 0
        while week < weeks:
            savings += 28 + (7 * week)
            week+=1
            
        if days > 0:
            savings += (days*(days+1))//2 + (days * week)
            
        return savings