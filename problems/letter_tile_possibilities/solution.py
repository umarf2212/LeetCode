class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        res = []
        for i in range(1, len(tiles)+1):
            res.append(list(permutations(tiles, i)))
        
        s = set()
        c = 0
        for item in res:
            for i in item:
                cur = ''.join(i)
                if cur not in s:
                    s.add(cur)
                    c+=1
        
        return c