class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return
        
        j = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j+=1
            
        nums[j] = nums[len(nums)-1]
        
        while(len(nums) != j+1):
            del nums[len(nums)-1]
