class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        c = 0
        s = Counter(arr)
        
        for char, count in s.items():
            if count == 1:
                c+=1
            
            if c == k:
                return char
        
        return ''