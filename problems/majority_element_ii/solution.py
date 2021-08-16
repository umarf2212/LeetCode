class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n3 = len(nums) // 3
        res = []
        nums.sort()
        
        # [3,2,3,1,2,2,3,5,6]
        # [1,2,2,2,3,3,3,5,6]
        curr = nums[0]
        count = 0
        for i in nums:
            
            if i == curr:
                count += 1
            else:
                if count > n3:
                    res.append(curr)
                    
                curr = i
                count = 1
        
        if count > n3:
            res.append(curr)
        
        return res