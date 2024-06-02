class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i+=1
        
        while i < len(self.intervals) and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i+=1
        
        new_intervals.append([left, right])

        while i < len(self.intervals):
            new_intervals.append(self.intervals[i])
            i+=1
        
        self.intervals = new_intervals
        

    def queryRange(self, left: int, right: int) -> bool:
        lo = 0
        hi = len(self.intervals)-1
        while lo <= hi:
            mid = (lo+hi) // 2

            if self.intervals[mid][0] <= left:
                lo = mid+1
            else:
                hi = mid-1
        
        # hi contains the overlapping interval
        
        if hi >= 0 and self.intervals[hi][0] <= left and self.intervals[hi][1] >= right:
            return True
        return False
        

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []

        for start, end in self.intervals:
            if end <= left or start >= right:
                new_intervals.append([start, end])
            else:
                if start < left:
                    new_intervals.append([start, left])
                
                if end > right:
                    new_intervals.append([right, end])
        
        self.intervals = new_intervals


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
