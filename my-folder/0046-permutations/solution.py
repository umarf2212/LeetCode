class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, S, ar, result):

            idx = len(S)

            if idx == len(nums):
                result.append(ar[:])
                return

            for i in range(len(nums)):
                if nums[i] not in S:
                    ar[idx] = nums[i]
                    S.add(nums[i])
                    backtrack(nums, S, ar, result)
                    S.remove(nums[i])

                    

        S = set()
        ar = [0] * len(nums)
        result = []
        backtrack(nums, S, ar, result)
        return result


