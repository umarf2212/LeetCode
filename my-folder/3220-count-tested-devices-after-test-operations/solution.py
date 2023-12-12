class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        
#         bp = batteryPercentages
#         n = len(bp)
#         count = 0
#         for i in range(n):
#             if bp[i] > 0:
#                 count += 1
                
#                 j = i+1
#                 while j < n:
#                     bp[j] = max(0, bp[j]-1)
#                     j+=1
#         return count

        bp = batteryPercentages
        n = len(bp)

        count = 0
        for i in range(n):
            if bp[i] > count:
                count += 1
            
        
        return count
    
