class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        # 1 2 3 4

        # O(k * n!)
        def backtracking(n, k, start, ans, S):

            if n < 0: 
                return
            
            # O(k)
            if n == 0 and len(S) == k:
                ans.append(list(S))
                return
            
            # O(N!)
            for i in range(start, 10):
                if i in S:
                    continue

                S.add(i)
                backtracking(n-i, k, i+1, ans, S)
                S.remove(i)
        
        ans = []
        S = set()
        backtracking(n, k, 1, ans, S)
        return ans
