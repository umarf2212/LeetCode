class Solution:
    def maximum69Number (self, num: int) -> int:
        
        s = str(num)
        st = ''
        for i in range(len(s)):
            if s[i] == '6':
                st += '9'
                break
            else:
                st += s[i]
        
        for j in range(i+1, len(s)):
            st += str(s[j])
                
        return int(''.join(st))
