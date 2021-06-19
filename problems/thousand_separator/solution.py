class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        n = str(n)
        sep = len(n)%3
        new = n[:sep]
        
        for i in range(sep, len(n)):
            if (i-sep)%3 == 0:
                new += '.'+n[i]
            else:
                new += n[i]
        
        if new[0] == '.':
            return new[1:]
        return new