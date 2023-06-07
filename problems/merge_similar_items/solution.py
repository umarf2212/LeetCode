class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        d = {}
        for item in (items1+items2):

            val = item[0]
            wt = item[1]

            if val not in d:
                d[val] = 0
            
            d[val] += wt
        
        return sorted([[val, wt] for val, wt in d.items()], key=lambda x:x[0])