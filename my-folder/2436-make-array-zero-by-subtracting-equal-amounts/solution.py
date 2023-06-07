import heapq
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        

        hq = [i for i in nums if i > 0]
        heapq.heapify(hq)
        ops = 0
        while hq:
            smallest = heapq.heappop(hq)

            new_q = []
            while hq:
                diff = heapq.heappop(hq)-smallest
                if diff > 0:
                    heapq.heappush(new_q, diff)
            
            ops += 1
            hq = new_q
            # print(hq)
        
        return ops
