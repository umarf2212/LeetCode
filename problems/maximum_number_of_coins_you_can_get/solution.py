class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        # 2 4 1 2 7 8
        # 1 2 2 4 7 8
        
        # 1 1 2 2 3 4 5 6 7 8 9 15
        
        piles.sort()
        
        res = 0
        bob = 0
        john = len(piles)-2
        while john > bob:
            res += piles[john]
            john -= 2
            bob += 1
        
        return res