class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        first = 0
        last = len(s)-1
        
        s = [i.lower() for i in s]
        
        while first < last:
            
            if not s[first].isalnum():
                first += 1
            
            if not s[last].isalnum():
                last -= 1
                
            
            if s[first].isalnum() and \
            s[last].isalnum():
                if s[first] != s[last]:
                    return False
                
                first += 1
                last -= 1
            
            
        return True
