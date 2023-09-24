class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num % 3 == 0:
            X = num//3
            return [X-1, X, X+1]
        
        return []

