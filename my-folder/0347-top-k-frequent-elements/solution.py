import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        pq = []
        for num, count in d.items():
            heapq.heappush(pq, (-count, num) )
        
        # print(pq)
        
        res = []
        while k:
            res.append(heapq.heappop(pq)[1])
            k-=1
        
        return res
        

        

