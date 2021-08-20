class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}        
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        res = []
        for num, count in d.items():
            res.append([count, num])
            
        res.sort(key=lambda x: x[0], reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(res[i][1])
        
        return ans