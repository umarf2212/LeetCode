class Solution:        
    def replaceDigits(self, s: str) -> str:
        
        return ''.join([s[i] if i%2==0 else 'abcdefghijklmnopqrstuvwxyz'[{'abcdefghijklmnopqrstuvwxyz'[i]:i for i in range(26)}[s[i-1]]+int(s[i])] for i in range(len(s))])
        