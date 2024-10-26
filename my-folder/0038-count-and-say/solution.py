class Solution:
    def countAndSay(self, n: int) -> str:

        # 1211
        # 111221
        def count(s):
            res = ''
            curChar = s[0]
            curCount = 0
            for ch in s:
                if ch == curChar:
                    curCount += 1
                else:
                    res += str(curCount) + curChar
                    curChar = ch
                    curCount = 1
            
            res += str(curCount) + curChar
            return res

        def sayCount(n):
            if n == 1:
                return '1'
            
            return count(sayCount(n-1))
        
        return sayCount(n)
