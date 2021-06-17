class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        
        res = []
        for i in range(len(arr2)):
            for el in [arr2[i]]*count[arr2[i]]:
                res.append(el)
                
            del count[arr2[i]]
            
        for key in sorted(count.keys()):
            for el in [key]*count[key]:
                res.append(el)
        
        return res