class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 2,3,1,2,5,6,2,3,2,2,2
        # 3,3,1,2,5,6,2,2,2,2,2
        # 3,3,1,6,5,2,2,2,2,2,2

        if len(nums) == 0: return
        
        last = len(nums) - 1
        while nums[last] == val:
            del nums[last]
            if last == 0: return
            last -= 1
        
        for i in range(len(nums)):
            
            if i > last: break
            
            if nums[i] == val:
                #swap
                temp = nums[i]
                nums[i] = nums[last]
                nums[last] = temp
                
                #find last
                last -= 1                  
                while nums[last] == val:
                    last -= 1
                    
        while nums[len(nums)-1] == val:
            del nums[len(nums)-1]
