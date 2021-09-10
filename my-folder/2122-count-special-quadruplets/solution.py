class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
                
        count = 0
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                for k in range(j+1,len(nums)-1):
                    for s in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] == nums[s]:
                            count+=1
                    
        
        return count
