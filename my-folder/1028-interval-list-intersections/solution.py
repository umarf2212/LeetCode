class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        m = len(firstList)
        n = len(secondList)
        
        i = 0
        j = 0
        result = []
        while i < m and j < n:

            # no overlap
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]

            if e1 < s2:
                i += 1
                continue
            
            elif e2 < s1:
                j += 1
                continue

            # overlap
            start = max(s1, s2)
            end = min(e1, e2)

            result.append([start, end])

            if e1 < e2:
                i += 1
            else:
                j += 1
        
        return result
