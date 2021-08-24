class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)-1
        
        k = k % len(nums)
        
        temp = []
        i = 0
        for i in range(len(nums)-1, n-k,-1):
            temp.append(nums[i])
        
        i-=1
        j = n
        while i >= 0:
            nums[j]  = nums[i]
            i-=1
            j-=1

        for i in range(k):
            nums[i] = temp.pop()
            

