class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        decoded = [first]
        prev = first
        for i in encoded:
            curr = prev ^ i
            decoded.append(curr)
            prev = curr
        
        return decoded
