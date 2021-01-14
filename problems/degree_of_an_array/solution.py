class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        # 1,2,2,3,4,2,1
        d = {}
        
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        # d = {1:2,2:3,3:1,4:1}
        
        maxVal = max(d.values())
        maxKeys = [key for key, val in d.items() if val == maxVal]
        
        # print(maxKeys)
        
        key=0
        diff = []
        while key < len(maxKeys):
            first = 0
            for i in range(len(nums)):
                if nums[i] == maxKeys[key]:
                    first = i
                    break
            
            last = 0
            for j in range(len(nums)-1,-1,-1):
                if nums[j] == maxKeys[key]:
                    last = j
                    break
                    
            diff.append(last - first + 1)
            
            key += 1
            
        
        return min(diff)