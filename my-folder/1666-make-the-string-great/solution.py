class Solution:
    def makeGood(self, s: str) -> str:
        # >>> ord('a')
        # 97
        # >>> ord('z')
        # 122
        # >>> ord('A')
        # 65
        # >>> ord('Z')
        # 90
        stack = [s[0]]
        
        for i in range(1, len(s)):
            
            if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()
            
            else:
                stack.append(s[i])
                
        return ''.join(stack)
