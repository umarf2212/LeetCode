class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Expand the window until it is satisfied
        # Now shrink until it is dissatisfied, while updating min answer
        # Start over
        
        t_count = Counter(t)
        required = len(t_count)
        l = 0
        r = 0
        window_chars = {}
        formed = 0
        ans = [float('inf'), -1, -1]
        # a:2, b:3, c:1
        # total 3 chars formed
        # requried = 3
        while r < len(s):
            
            char = s[r]
            
            if char not in window_chars:
                window_chars[char] = 0
            window_chars[char] += 1
            
            if char in window_chars and window_chars[char] == t_count[char]:
                formed += 1
            
            # window satisfied
            if formed == required:
                
                while l <= r and formed == required:
                    
                    # we have the answer here
                    # ans = [size, l, r] ; size = r-l+1
                    if ans[0] > r-l+1:
                        ans = [r-l+1, l, r]
                    
                    window_chars[s[l]] -= 1
                    
                    if s[l] in t_count and window_chars[s[l]] < t_count[s[l]]:
                        formed -= 1
                    
                    l += 1
            
            r+=1
        
        if ans[0] == float('inf'):
            return ''
        
        return s[ans[1]:ans[2]+1]
        
