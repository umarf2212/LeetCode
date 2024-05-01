class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']

        stack = []

        for token in tokens:

            if token not in operators:
                stack.append(token)
            
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if token == '+':
                    res = a + b
                
                elif token == '-':
                    res = a - b
                
                elif token == '*':
                    res = a * b
                
                elif token == '/':
                    res = a/b
                
                stack.append(res)
        
        return int(stack[0])
