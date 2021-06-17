class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        minDistance = float('inf')
        
        i=0
        while i <= len(nums)//2:
            if nums[i] == target:
                if abs(i-start) < minDistance:
                    minDistance = abs(i-start)
            
            if nums[len(nums)-1-i] == target:
                if abs(len(nums)-1-i-start) < minDistance:
                    minDistance = abs(len(nums)-1-i-start)
            
            i+=1
        
        return minDistance
