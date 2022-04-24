class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        odd = sorted([nums[i] for i in range(len(nums)) if i%2!=0],reverse=True)
        even = sorted([nums[i] for i in range(len(nums)) if i%2==0])
        
        i = 0
        j = 0
        
        res = []
        while i<len(odd) and j<len(even):
            res.append(even[j])
            res.append(odd[i])
            
            i+=1
            j+=1
        
        if i<len(odd): res.append(odd[i])
        if j<len(even): res.append(even[j])
        
        return res
