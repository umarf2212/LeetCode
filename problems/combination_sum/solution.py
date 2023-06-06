class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(cand, target, start, ar, ans):

            if target < 0:
                return
            
            # O(N)
            elif target == 0:
                ans.append([i for i in ar])
                return 

            # O(N!)
            for i in range(start, len(cand)):
                # we are avoiding the case where we don't take 
                # current element and recurse further. That is 
                # because we are using start which will eventually 
                # decrease the range of array anyways and skip elements
                # along the way.
                ar.append(cand[i])
                backtrack(cand, target-cand[i], i, ar, ans)
                ar.pop()
        
        ar = []
        ans = []
        backtrack(candidates, target, 0, ar, ans)
        return ans
