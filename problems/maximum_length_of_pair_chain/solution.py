class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        
        pairs.sort(key=lambda pair:pair[0])
        
        dp = [1 for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    
        
        # print(dp)
        return max(dp)