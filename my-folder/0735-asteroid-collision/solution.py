class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        # 5 10 -5

        # 10 2 -5

        # -2 -1 1 2

        # -1 2 4 -5 6 -3 2 -1

        # -1 -2 2 -3 4
        
        stack = []
        for i in range(len(asteroids)):
            ast = asteroids[i]
            
            if ast > 0:
                stack.append(ast)
            else:

                while stack and stack[-1] > 0 and stack[-1] < abs(ast):
                    stack.pop()
                
                if stack and stack[-1] == abs(ast):
                    stack.pop()
                    continue
                
                if stack and stack[-1] > 0 and stack[-1] > abs(ast):
                    continue
                
                stack.append(ast)
        
        return stack
            

