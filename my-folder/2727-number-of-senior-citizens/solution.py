class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len(list(filter(lambda x:int(x[11:13]) > 60, details)))
