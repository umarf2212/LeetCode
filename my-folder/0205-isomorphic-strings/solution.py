class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d1 = {}
        ar = [i for i in s]
        for i in range(len(ar)):
            if ar[i] in d1:
                d1[ar[i]].append(i)
            else:
                d1[ar[i]] = [i]
                
        d2 = {}
        ar = [i for i in t]
        for i in range(len(ar)):
            if ar[i] in d2:
                d2[ar[i]].append(i)
            else:
                d2[ar[i]] = [i]
        
        if len(d1.values()) != len(d2.values()): return False
        for i in range(len(d1.values())):
            if list(d1.values())[i] != list(d2.values())[i]:
                return False
            
        return True
        
