class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        @cache
        def f(n):
            if n<=1: return 1
            return n * f(n-1)
        
        def comb(n, r):
            return f(n) // (f(r) * f(n-r))
        
        numCounts = Counter(nums)
        
        totalCount = 0
        
        for num, count in numCounts.items():
            if count > 1:
                totalCount += comb(count, 2)
            
        return totalCount
