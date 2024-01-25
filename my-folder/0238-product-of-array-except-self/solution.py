class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 2 3 4 5
        # 1 2

        n = len(nums)
        
        preduct = [1]
        for i in range(1, n):
            preduct.append( nums[i-1] * preduct[-1] )

        # product = [1]
        # for i in range(n-2, -1, -1):
        #     product.append( nums[i+1] * product[-1] )
        # product = product[::-1]
        
        product = [1 for _ in range(n)]
        for i in range(n-2, -1, -1):
            product[i] = product[i+1] * nums[i+1]
        
        # print(preduct)
        # print(product)
        
        res = []
        for i in range(n):
            res.append(preduct[i] * product[i])
        
        return res
