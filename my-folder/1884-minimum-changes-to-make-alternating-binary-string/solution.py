class Solution:
    def minOperations(self, s: str) -> int:
        
        s1 = [1 ^ 1 & i for i in range(len(s))]
        s2 = [1 & i for i in range(len(s))]

        # for i in range(len(s)):
        #     s1[i] = abs(s1[i] - int(s[i]))
        #     s2[i] = abs(s2[i] - int(s[i]))
        
        sub = lambda x: abs(x[0]-int(x[1]))
        
        s1 = [sub(i) for i in zip(s1,s)]
        s2 = [sub(i) for i in zip(s2,s)]

        
        # print(s1,s2)
    
        return(min(sum(s1), sum(s2)))
