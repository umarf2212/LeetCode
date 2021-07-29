class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 != 0:
                break
        else:
            return ""
            
        return num[:i+1]
        
        # 1 2 3 4 5 6 7  4 6 0