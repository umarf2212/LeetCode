class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # n = 4; k = 2
        # 1 2 3 4

        def generate(n, k, start, l, ar, ans):

            if l == k:
                ans.append(ar[:])
                return

            for i in range(start, n+1):
                ar.append(i)
                generate(n, k, i+1, l+1, ar, ans)
                ar.pop()
        
        ar = []
        ans = []
        generate(n, k, 1, 0, ar, ans)
        return ans