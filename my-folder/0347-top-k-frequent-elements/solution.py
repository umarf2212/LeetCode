class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}        
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        priority_q = []
        
        for num, count in d.items():
            priority_q.append((-count, num))
            
        heapq.heapify(priority_q)
        
        res = []
        while k > 0:
            res.append(heapq.heappop(priority_q)[1])
            k-=1
            
        return res
