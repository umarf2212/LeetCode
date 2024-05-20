class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        
        def calcXOR(nums, i, cur, ans):
            if i == len(nums):
                ans.append(cur)
                return
            
            calcXOR(nums, i+1, cur ^ nums[i], ans)
            calcXOR(nums, i+1, cur, ans)
        
        ans = []
        calcXOR(nums, 0, 0, ans)
        return sum(ans)

