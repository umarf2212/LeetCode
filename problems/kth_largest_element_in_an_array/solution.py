import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [-i for i in nums]
        heapq.heapify(heap)
        res = -1
        while k:
            res = heapq.heappop(heap)
            k -= 1
        
        return -res