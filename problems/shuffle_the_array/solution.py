class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        ar = []
        for i in range(n):
            ar.append(nums[i])
            ar.append(nums[n+i])
            
        return ar