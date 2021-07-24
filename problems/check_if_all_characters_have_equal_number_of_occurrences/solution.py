class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = Counter(s)
        c = counts[s[0]]
        for count in counts.values():
            if count != c:
                return False
            
        return True