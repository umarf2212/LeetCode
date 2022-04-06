class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(arr, target):
            d = {}
            pairs = set()
            for i in range(len(arr)):
                p = target - arr[i]
                if p in d:
                    pairs.add(tuple([p, arr[i]]))
                else:
                    d[arr[i]] = i
            
            return pairs
        
        d = {}
        res = set()
        for i in range(len(nums)):
            
            if nums[i] not in d:
                d[nums[i]] = i
                pairs = twoSum(nums[i+1:], -nums[i])
                for pair in pairs:
                    res.add(tuple(sorted([nums[i], pair[0], pair[1]])))
        
        return res
