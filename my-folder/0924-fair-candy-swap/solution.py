class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        sumA = sum(A)
        sumB = sum(B)
        
        diff = abs(sumA - sumB) // 2
        
        large = A if sumA > sumB else B
        small = A if sumA < sumB else B
        
        small = {i:0 for i in small}
        
        for i in large:
            if i - diff in small:
                return [i, i-diff] if large == A else [i-diff, i]
