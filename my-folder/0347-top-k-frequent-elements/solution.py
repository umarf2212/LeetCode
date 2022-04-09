class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        C = Counter(nums)
        
        ar = []
        for num, count in C.items():
            ar.append([count, num])
        
        ar.sort(key=lambda x: x[0], reverse=True)
        
        res = []
        for i in range(k):
            res.append(ar[i][1])
        
        return res
