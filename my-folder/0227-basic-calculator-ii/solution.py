class Solution:
    
    def splitSign(self, st):
        prev = ''
        ar=[]
        for i in st:
            if i != ' ':
                if i in {'+':1,'-':1,'/':1,'*':1}:
                    ar.append(prev)
                    ar.append(i)
                    prev=''
                else:
                    prev += i
            
        if len(prev) > 0: ar.append(prev)
        return ar
    
    def cal(self, nums, opr):
        
        stack = []
        
        for i in range (len(nums)):
            if len(stack) > 0 and (stack[-1] == opr[0] or stack[-1] == opr[1]):
                operator = stack.pop()
                
                left = int(stack.pop())
                right = int(nums[i])
                
                if operator == '*':
                    res = left * right
                elif operator == '/':
                    res = left // right
                elif operator == '+':
                    res = left + right
                elif operator == '-':
                    res = left - right
                    
                stack.append(str(res))
            
            else:
                stack.append(nums[i])
                
        return stack
                
                    
    def calculate(self, s: str) -> int:
        
        nums = self.splitSign(s)
        
        nums = self.cal(nums, ['/','*'])
        nums = self.cal(nums, ['-','+'])

        # print(nums)
        
        return int(nums[0])
    
