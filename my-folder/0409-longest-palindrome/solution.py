class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = Counter(s)
        
        total = 0
        odd = 0
        
        for val in d.values():
            if val % 2 == 0:
                total += val
            else:
                total += val - 1
                odd = 1
        # print(d)
        return total+odd
