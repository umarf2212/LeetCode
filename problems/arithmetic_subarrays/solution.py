class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        res = []
        for i in range(len(l)):
            ar = nums[l[i]:r[i]+1]
            ar.sort()
            diff = ar[1] - ar[0]
            
            curr = True
            for j in range(len(ar)-1):
                if ar[j+1] - ar[j] != diff:
                    curr = False
                    break
            
            res.append(True and curr)
    
        return res
            
            