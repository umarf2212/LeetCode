class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        # The idea is to sort the intervals and find the maximum number 
        # of overlapping intervals at a certain point. 
        # These overlapping intervals will have to be in separate groups.
        # This Sweep Line algorithm is new to me.
        # Kudos to me for learning it finally.

        # This Sweep line algorithm code is pretty self explanatory.
        # For every start, we simply increment the count. 
        # For every end, we decrement.
        # This will effectively calculate how many intervals start at some point.
        
        events = []
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1], -1))
        
        events.sort(key = lambda x:(x[0], -x[1]))

        maxOverlaps = 1
        curOverlaps = 0
        for event in events:
            curOverlaps += event[1]
            maxOverlaps = max(maxOverlaps, curOverlaps)
        
        return maxOverlaps





        



        # x---------.--y
        #    a------.---------b
        #       p---.-------q
        #                s-------t
