class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        # 1 2 3 4 5 6 7 1
        # k = 3

        curWindow = sum(cardPoints[:k])

        ans = curWindow
        for i in range(k):
            curWindow = curWindow - cardPoints[k-1-i] + cardPoints[-i-1]
            ans = max(curWindow, ans)
        
        return ans
            

