class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        # 48-57
        
        num = float('-inf')
        for char in s.split(' '):
            if ord(char[0]) >= 48 and ord(char[0]) <= 58:
                curr = int(char)
                if curr > num:
                    num = curr
                else:
                    return False
        
        return True
