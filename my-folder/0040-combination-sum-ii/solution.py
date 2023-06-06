class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # 1 1 2 3 3 4

        def backtrack(cand, target, start, ar, ans):

            if target < 0:
                return

            if target == 0:
                ans.append(ar[:])
                return

            for i in range(start, len(cand)):
                if i > start and cand[i-1] == cand[i]:
                    continue

                ar.append(cand[i])
                backtrack(cand, target-cand[i], i+1, ar, ans)
                ar.pop()
        
        ar = []
        ans = []
        candidates.sort()
        backtrack(candidates, target, 0, ar, ans)
        return ans
