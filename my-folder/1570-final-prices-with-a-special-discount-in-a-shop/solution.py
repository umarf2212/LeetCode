class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        # Nearest smaller to the right
        stack = []
        res = []
        for i in range(len(prices)-1,-1,-1):

            while stack and stack[-1] > prices[i]:
                stack.pop()
            
            if stack:
                res.append(prices[i]-stack[-1])
            else:
                res.append(prices[i])
            
            stack.append(prices[i])
        
        res = res[::-1]
        return res

