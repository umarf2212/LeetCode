class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        
        addDigits = lambda num: str(sum([int(i) for i in str(num)]))
        
        d = {}
        maxBalls = float('-inf')
        for ball in range(lowLimit, highLimit+1):
            ball = addDigits(ball)
            if ball in d:
                d[ball] += 1
            else:
                d[ball] = 1
                
            if d[ball] > maxBalls:
                maxBalls = d[ball]
        
        # for ball, count in d.items():
        #     if count > maxBalls:
        #         maxBalls = count
        
        return maxBalls
