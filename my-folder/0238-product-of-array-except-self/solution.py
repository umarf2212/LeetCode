class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # 2 3 4 5
        # 1  2  6 24 -> left
        # 60 20 5 1 -> right
        
        product_left = 1
        
        product_right = [1]
        for i in range(len(nums)-2, -1, -1):
            product_right.append(product_right[-1] * nums[i+1])
                
        res = []
        n = len(nums)
        for i in range(n):
            res.append(product_left * product_right[n-1-i])
            product_left *= nums[i]
            
        return res
