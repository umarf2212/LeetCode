class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        R = len(nums)
        C = len(nums[0])
        
        if r*c != R*C: return nums
        
        #flatten the matrix
        flat = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                flat.append(nums[i][j])
        
        res = []
        cs = 0
        for i in range(r):
            res.append(flat[cs:cs+c])
            cs += c
        return res
