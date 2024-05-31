class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # n = 2
        # (
        
        # (
        # n = 1, open = 1

        # ()
        # n=1, open = 0

        # At any given point, we can either open a bracket, or close existing one
        # We can only open if n > 0
        # We can only close if curOpen > 0 : open is how many are currently open

        def generate(n, curOpen, cur, res):

            if n == 0 and curOpen == 0:
                res.append(''.join(cur))
                return

            if n > 0:
                cur.append('(')
                generate(n-1, curOpen+1, cur, res)
                cur.pop()
            
            if curOpen > 0:
                cur.append(')')
                generate(n, curOpen-1, cur, res)
                cur.pop()
            
            
        res = []
        cur = []
        generate(n, 0, cur, res)
        return res

