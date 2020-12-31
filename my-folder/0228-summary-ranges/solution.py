class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        prev = []
        ret = []
        
        for i in range(len(nums)):
            
            if len(prev) == 0 or nums[i] == prev[-1] + 1:
                prev.append(nums[i])
                
            else:
                if len(prev) == 1:
                    ret.append(str(prev[0]))
                else:
                    ret.append(str(prev[0])+"->"+str(prev[-1]))
                
                prev = [nums[i]]
        
        if len(prev) > 0:
            if len(prev) == 1:
                ret.append(str(prev[0]))
            else:
                ret.append(str(prev[0])+"->"+str(prev[-1]))
            
                    
        return ret
