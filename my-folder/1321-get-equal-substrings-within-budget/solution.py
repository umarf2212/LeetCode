class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        if maxCost == 0:
            return len(s) if s == t else 1

        
        # abcd
        # bcdf

        # 1. Find the ASCII difference of each char s[i] and t[i] and store it in an array.
        # 2. Find the longest subarray that sums up to maxCost


        # [1,2,3,1,2,1,2,8,10]

        # prefix sum: [1,3,6,7,9,10,12,20,30]

        diff = []
        for i in range(len(s)):
            diff.append( abs(ord(s[i]) - ord(t[i])) )

        i = 0
        curSum = 0
        maxSubarrayLen = 0
        for j in range(len(diff)):
            curSum += diff[j]


            while curSum > maxCost:
                curSum -= diff[i]
                i += 1
            

            maxSubarrayLen = max(maxSubarrayLen, j-i+1)

        return maxSubarrayLen



