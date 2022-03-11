class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        
        poison = 0
        
        for i in range(1, len(timeSeries)):
            diff = timeSeries[i] - timeSeries[i-1]
            
            if diff >= duration:
                poison += duration
            else:
                poison += diff
        
        poison += duration
        
        return poison