class Solution:
    def myAtoi(self, s: str) -> int:
        
        MIN = -2**(31)
        MAX = 2**(31)-1
        n = len(s)
        int0 = ord('0')
        int9 = ord('9')

        # 1. Determine the sign
        # 2. Start reading the first contiguous set of valid numbers

        # Determine Sign
        i = 0
        sign = 1
        while i < n:
            # ignore leading whitespace
            if s[i] == ' ':
                i+=1
                continue

            # if first - sign appears followed by an integer
            if i < n-1 and s[i] == '-' and int0 <= ord(s[i+1]) <= int9:
                sign = -1
                i+=1
                break
            
            # if first + sign appears followed by a number
            if i < n-1 and s[i] == '+' and int0 <= ord(s[i+1]) <= int9:
                i+=1
                break
            
            # if first integer appears 
            if ord(s[i]) in range(int0, int9+1):
                break
            
            # break for anything else
            else:
                return 0

            i+=1
        
        num = 0
        # at this point, i is possibly at a number
        while i < n and int0 <= ord(s[i]) <= int9:
            curNum = ord(s[i]) - 48
            num = num * 10 + curNum
            i+=1
        
        finalNum = num * sign

        if finalNum < MIN: return MIN
        if finalNum > MAX: return MAX
        
        return finalNum


