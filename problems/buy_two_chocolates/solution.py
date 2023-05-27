class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        for i in range(len(prices)-1):
            curDiff = money - (prices[i] + prices[i+1])
            
            if curDiff >= 0:
                return curDiff
        
        return money