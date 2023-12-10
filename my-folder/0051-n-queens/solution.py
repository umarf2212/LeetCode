class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        def copyBoard(cur, res):
            temp = []
            for row in cur:
                temp.append(''.join(row))
            res.append(temp)
        
        def gen(cur, hsc, hsul, hsur, n, res):
            r = len(hsc)

            if r == n:
                copyBoard(cur, res)
                return
            
            for c in range(n):

                if c in hsc: continue
                if r-c in hsul: continue
                if r+c in hsur: continue

                hsc.add(c)
                hsul.add(r-c)
                hsur.add(r+c)
                cur[r][c] = 'Q'

                gen(cur, hsc, hsul, hsur, n, res)

                hsc.remove(c)
                hsul.remove(r-c)
                hsur.remove(r+c)
                cur[r][c] = '.'
        
        hsc = set()
        hsul = set()
        hsur = set()
        cur = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        gen(cur, hsc, hsul, hsur, n, res)
        return res



            
