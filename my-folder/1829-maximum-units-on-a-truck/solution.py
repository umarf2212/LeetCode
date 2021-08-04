class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x:x[1], reverse=True)
        
        totalUnits = 0
        for boxType in boxTypes:
            
            if boxType[0] >= truckSize:
                totalUnits += truckSize * boxType[1]
                break
            else:
                totalUnits += boxType[0] * boxType[1]
                truckSize -= boxType[0]
            
        return totalUnits
