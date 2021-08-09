class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        heap = [-i for i in score]
        
        heapq.heapify(heap)
        
        d = {}
        
        d[heapq.heappop(heap)] = 'Gold Medal'
        if heap: d[heapq.heappop(heap)] = 'Silver Medal'
        if heap: d[heapq.heappop(heap)] = 'Bronze Medal'
        
        position = 4
        while heap:
            d[heapq.heappop(heap)] = str(position)
            position += 1
        
        return [d[-i] for i in score]


        
