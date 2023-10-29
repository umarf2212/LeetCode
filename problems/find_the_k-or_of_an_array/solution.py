class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        
        ans = 0
        
        for bit in range(32):
            c = 0
            
            for num in nums:
                if (num >> bit) & 1:
                    c += 1
            
            if c >= k:
                ans = ans | (1 << bit)
        
        return ans
        