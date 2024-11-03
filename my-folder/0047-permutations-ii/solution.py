from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, ar, C, idx, result):
            
            if idx == len(nums):
                result.append(ar[:])
            
            for num, count in C.items():
                if count > 0:
                    ar[idx] = num
                    C[num] -= 1
                    backtrack(nums, ar, C, idx+1, result)
                    C[num] += 1
        
        C = Counter(nums)
        ar = [0] * len(nums)
        result = []
        backtrack(nums, ar, C, 0, result)
        return result
