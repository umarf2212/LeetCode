from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        return -1 if 1 in Counter(tasks).values() else sum([(count-1)//3+1 for count in Counter(tasks).values()])

