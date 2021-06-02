class Solution:
    
    def charToBool(self, char):
        return True if char=='t' else False
    
    def evalAnd(self, ar):
        prev = ar[0]
        for i in range(1, len(ar)):
            prev = prev and ar[i]
        return prev
    
    def evalOr(self, ar):
        prev = ar[0]
        for i in range(1, len(ar)):
            prev = prev or ar[i]
        return prev
    
    def evalNot(self, char):
        return not char[0]
    
    def parse(self, exp):
        
        stack = []
        charMap = set(['|', '&', '!', 't', 'f'])
        
        for i in range(len(exp)):
            if exp[i] == '(' or exp[i] == ',':
                continue
            
            elif exp[i] == 't' or exp[i] == 'f':
                stack.append(self.charToBool(exp[i]))
                
            elif exp[i] == '&' or exp[i] == '|' or exp[i] == '!':
                stack.append(exp[i])
                
            else:
                #process
                item = stack.pop()
                ar = []
                while item == True or item == False:
                    ar.append(item)
                    item = stack.pop()

                if item == '|':
                    stack.append(self.evalOr(ar))
                elif item == '&':
                    stack.append(self.evalAnd(ar))
                elif item == '!':
                    stack.append(self.evalNot(ar))
        
        return stack[0]
    
    def parseBoolExpr(self, expression: str) -> bool:
        return self.parse(expression)
