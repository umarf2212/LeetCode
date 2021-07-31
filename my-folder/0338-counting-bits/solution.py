class Solution:
    def countBits(self, n: int) -> List[int]:
        return [sum([int(i) for i in str(bin(digit))[2:]]) for digit in range(n+1)]
