class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return max([len(citations)-i if len(citations)-i <= c else 0 for i, c in enumerate(sorted(citations))])
