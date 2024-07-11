class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        # (u(love)i)
        # uevoli

        stack = ['']
        for i in range(len(s)):
            ch = s[i]

            if ch == '(':
                stack.append('')
            
            elif ch == ')':
                lastStr = stack.pop()
                stack[-1] += lastStr[::-1]
            
            else:
                stack[-1] += ch
        
        # print(stack)
        return stack[-1]
