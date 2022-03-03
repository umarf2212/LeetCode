class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        neg = []
        pos = []
        
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        
        i=0
        res = []
        while i < len(nums)//2:
            res.append(pos[i])
            res.append(neg[i])
            i+=1
        
        return res
