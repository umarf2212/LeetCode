class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        d = {}
        lenA = len(A)
        for word in range(lenA):
            for char in range(len(A[word])):
                if A[word][char] not in d:
                    d[A[word][char]] = [0] * lenA
                    d[A[word][char]][word] = 1

                else:
                    d[A[word][char]][word] += 1
        

        res = []
        for key, val in d.items():
            if all(val):
                res += [key] * min(val)
                
        return res
