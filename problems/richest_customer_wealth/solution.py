class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxWealth = 0
        for customer in accounts:
            total = 0
            for i in customer:
                total+=i
            if total > maxWealth:
                maxWealth = total
        
        return maxWealth