class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        def backtrack(nums, i, cur, res):
            if i == len(nums):
                res.add(tuple(cur[:]))
                return
            
            cur.append(nums[i])
            backtrack(nums, i+1, cur, res)
            cur.pop()

            backtrack(nums, i+1, cur, res)
        
        res = set()
        cur = []
        backtrack(nums, 0, cur, res)
        return [list(subset) for subset in res]
