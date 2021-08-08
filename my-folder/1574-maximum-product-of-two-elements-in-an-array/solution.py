class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        heap = [-i for i in nums]
        
        heapq.heapify(heap)
        
        return (-(heapq.heappop(heap))-1) * (-(heapq.heappop(heap))-1)
