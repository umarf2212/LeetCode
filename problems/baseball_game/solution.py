class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        score = []
        
        for op in ops:
            print(score)
            if op[-1].isdigit():
                
                if op[0] == "-":
                    op = int(op[1:]) * -1
                else:
                    op = int(op)
                    
                score.append(op)
            
            elif op == "+":
                score.append(score[-1]+score[-2])
            
            elif op == "D":
                score.append(score[-1]*2)
            
            elif op == "C":
                score.pop()
        
        print(score)
        return sum(score)