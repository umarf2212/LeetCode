class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def getXOR(ar):
            res = 0
            for i in ar: res ^= i
            return res
        
        ans = 0
        for r in range(1, len(nums)+1):
            for com in combinations(nums, r):
                ans += getXOR(com)
        
        return ans
        