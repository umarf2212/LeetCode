class Solution:
    def reverseWords(self, s: str) -> str:
        
        # the sky is blue     
        
        res = ''
        left = None
        right = None
        for i in range(len(s)-1, -1, -1):
            
            if s[i] != ' ':
                if right == None:
                    right = i
            
            else:
                if right != None:
                    left = i+1
            
            if left and right:
                res += s[left:right+1] + ' '
                
                left = None
                right = None
        
        if right != None:
            res += s[0:right+1] + ' '
        
        return res[:len(res)-1]
