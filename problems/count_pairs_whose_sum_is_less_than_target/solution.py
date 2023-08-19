class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        # [-1,1,2,3,1]
        # -1 1 1 2 3
        
        # [-6,2,5,-2,-7,-1,3]
        
        # -7 -6 -2 -1 2 3 5
        
        
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                Sum = nums[i] + nums[j]
                
                if Sum < target:
                    count += 1
        
        return count