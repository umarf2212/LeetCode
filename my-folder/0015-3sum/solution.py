class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        result = set()
        
        for i in range(len(nums)):
            
            j = i+1
            k = len(nums)-1
            
            while j < k:
                
                Sum = nums[i] + nums[j] + nums[k]
                
                if Sum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                
                elif Sum < 0:
                    j += 1
                    
                else:
                    k -= 1
                    
        
        return result
