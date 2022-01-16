class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        dq = deque([-1] * len(nums))
        
        for i in range(len(nums)):
            
            if dq[index[i]] == -1:            
                dq[index[i]] = nums[i]
            else:
                dq.insert(index[i], nums[i])
            
        return [i for i in dq if i is not -1]