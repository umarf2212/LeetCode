import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        n = len(arr)
        heap = []

        for i in range(n):
            for j in range(i+1, n):
                heapq.heappush(heap, (arr[i]/arr[j], arr[i], arr[j]) )
        
        last = []
        while k > 0:
            last = heapq.heappop(heap)
            k -= 1
        
        return [last[1], last[2]]

