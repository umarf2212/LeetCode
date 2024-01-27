class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # 1 -2 4 3 -2 1 4 -1 2


        max_prod = nums[0]
        min_prod = nums[0]
        res = max_prod
        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            res = max(res, max_prod)
        
        return res
