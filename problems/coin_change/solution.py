class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Recurrence Relation
        # M(i, amount) = min( M(i-1, curAmount), 1 + M(i, curAmount-coin[i]) )
        
        # Classic 0/1 problem of choose or not choose

        n = len(coins)

        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]

        #no coins needed for 0 amount
        dp[0][0] = 0 

        # with no coins, no amount can be made
        # inf is the *right* placeholder as per the "RR"
        for i in range(1, amount+1):
            dp[0][i] = float('inf')
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i][j] = min( dp[i-1][j], 1 + dp[i][j-coins[i-1]] )
                else:
                    dp[i][j] = dp[i-1][j]
        
        if dp[n][amount] == float('inf'):
            return -1
        
        return dp[n][amount]



