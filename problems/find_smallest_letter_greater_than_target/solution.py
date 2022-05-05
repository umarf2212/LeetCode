class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        i=0
        while True:
            if letters[i] > target:
                return letters[i]
            
            i+=1
            
            if i == len(letters):
                return letters[0]