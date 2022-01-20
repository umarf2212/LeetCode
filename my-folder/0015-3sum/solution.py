class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        result = set()
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            
            j = i+1
            k = len(nums)-1
        
            while j < k:
                Sum = nums[i] + nums[j] + nums[k]

                if Sum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    
                    j += 1
                    k -= 1

                elif Sum < 0:
                    j += 1

                else:
                    k -= 1
        
        return result
