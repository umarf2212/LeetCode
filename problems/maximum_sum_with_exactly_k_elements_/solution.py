import heapq
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        
        heap = [-i for i in nums]
        heapq.heapify(heap)
        
        Sum = 0
        for _ in range(k):
            num = -heapq.heappop(heap)
            Sum += num
            heapq.heappush(heap, -(num+1))
        
        return Sum