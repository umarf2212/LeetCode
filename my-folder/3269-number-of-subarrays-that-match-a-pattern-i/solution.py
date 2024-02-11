class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        
        # nums = [1,2,3,4,5,6]; size = n
        # pattern = [1,1]; size = p
        
        # The window size for the subarray is p+1
        
        # nums = [1,4,4,1,3,5,5,3]
        # pattern = [1,0,-1]
        
        # [1, 4, 4, 1, 3, 5, 5, 3]
        # [_, 1, 0, -1, 1, 1, 0, -1]
        
        n = len(nums)
        p = len(pattern)
        
        numsP = [None]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                numsP.append(1)
            elif nums[i] == nums[i-1]:
                numsP.append(0)
            else:
                numsP.append(-1)
        
        ans = 0
        for i in range(1, n-p+1):
            for j in range(i, i+p):
                if numsP[j] != pattern[j-i]:
                    break
            else:
                ans += 1
                
        return ans   
                
