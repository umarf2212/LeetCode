class Solution:
    def secondHighest(self, s: str) -> int:
        
        # 1. Using Set
        
        st = set()
        
        for i in s:
            if i.isnumeric():
                st.add(int(i))
        
        ar = sorted(list(st), reverse=True)
        
        return ar[1] if len(ar)>1 else -1
