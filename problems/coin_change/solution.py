class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        '''
        Recurrence Relation:
        M(i,j) = min( M(i-1, j) , 1 + M(i, j-coins[i]) )
        
        '''
        
        n = len(coins)
        
        dp = [0] + [float('inf') for _ in range(amount)]
        
        # 0 amount -> coins = 0
        # 0 amount -> coins > 0 -> float('inf')
        
        # dp[0][i] -> float('inf')
        # dp[i][0] -> 0 amount        
    
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[j] = min(dp[j], 1 + dp[j - coins[i-1]])
          
        
        return dp[amount] if dp[amount] != float('inf') else -1