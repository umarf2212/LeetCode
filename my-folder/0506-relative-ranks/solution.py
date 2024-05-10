class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        scores = [(i, score[i]) for i in range(len(score))]
        scores.sort(key = lambda x:x[1], reverse=True)

        ranks = {}
        for j in range(len(scores)):
            rank = j+1

            if rank == 1:
                rank = 'Gold Medal'
            elif rank == 2:
                rank = 'Silver Medal'
            elif rank == 3:
                rank = 'Bronze Medal'
            
            ranks[ scores[j][0] ] = str(rank)
        
        res = []
        for i in range(len(score)):
            res.append(ranks[i])
        
        return res





        
