class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        if not arr:
            return []
        

        sorted_arr = sorted(arr)
        curRank = 1
        ranks = {}

        ranks[sorted_arr[0]] = 1
        for num in sorted_arr:
            if num not in ranks:
                curRank += 1
                ranks[num] = curRank
        

        res = []
        for num in arr:
            res.append(ranks[num])
        
        return res

