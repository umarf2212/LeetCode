class Solution:
    def frequencySort(self, s: str) -> str:
        
        d = Counter(s)
        
        heap = [(-count, key) for key, count in d.items()]
        
        heapq.heapify(heap)
        
        newStr = ''
        while heap:
            st = heapq.heappop(heap)
            newStr += st[1] * -st[0]
        
        return newStr
