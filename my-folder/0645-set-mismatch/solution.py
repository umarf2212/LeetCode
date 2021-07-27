class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        dup = -1
        s = set()
        n = len(nums)
        for i in range(n):
            
            if nums[i] in s:
                dup = nums[i]
            else:
                s.add(nums[i])
                
        return [dup, (n*(n+1))//2 - sum(s)]
