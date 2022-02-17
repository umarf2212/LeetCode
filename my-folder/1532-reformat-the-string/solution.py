class Solution:
    def reformat(self, s: str) -> str:
        
        # 0-9 => 48 - 57
        # a-z => 97 - 122
        
        alpha = []
        num = []
        
        for i in s:
            if i.isnumeric():
                num.append(i)
            else:
                alpha.append(i)
        
        if abs(len(alpha) - len(num)) > 1:
            return ''
        
        
        res=''
        i=0
        j=0
        
        if len(alpha) > len(num):
            pair = [alpha, num]
        else:
            pair = [num, alpha]
            
        while i < len(alpha) and j < len(num):
            res += pair[0][i] + pair[1][i]
            i+=1
            j+=1
        
        if i < len(alpha):
            res += alpha[i]
        elif j < len(num):
            res += num[j]
        
        return res
