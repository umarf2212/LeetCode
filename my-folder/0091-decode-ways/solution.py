class Solution:
    def numDecodings(self, s: str) -> int:
        
        # ~RR: dp[i] = dp[i] + 1, dp[i] = dp[i-1] + dp[i] + 1

        # We are also accounting for the empty string
        # '' => there is only one way to decode an empty string
        # '' => 1
        # So we need to build a dp table of size n+1:
        # dp[0] for the empty string and dp[1:n+1] for n size string


        n = len(s)
        dp = [0] * (n+1)
        
        # empty string
        dp[0] = 1
        
        # first char
        dp[1] = 0 if s[0] == '0' else 1 

        for i in range(2, n+1):

            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
