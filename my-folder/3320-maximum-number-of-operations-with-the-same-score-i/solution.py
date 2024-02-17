class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        
        score = nums[0]+nums[1]
        
        nums = nums[::-1]
        
        # print(score)
        ops = 0
        while len(nums) > 1:
            a = nums.pop()
            b = nums.pop()
            
            if a+b == score:
                ops += 1
            else:
                break
        
        return ops
