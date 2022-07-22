class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]+nums[i])
        
        # print(prefix)
        
        minLen = float('inf')
        
        for i in range(len(prefix)):
            if prefix[i] >= target:
                minLen = i + 1
                break
        
        i = 0
        j = 0
        while i <= j and j < len(prefix):
            diff = prefix[j] - prefix[i]
            
            if diff >= target:
                minLen = min(minLen, j-i)
                while i < j and prefix[j]-prefix[i] >= target:
                    minLen = min(minLen, j-i)
                    i+=1
            else:
                j += 1
        
        return minLen if minLen != float('inf') else 0
