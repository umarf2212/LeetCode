class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-(i) for i in stones]
        heapq.heapify(heap)

        
        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)

            heapq.heappush(heap, a-b)
        
        return -(heap[0])