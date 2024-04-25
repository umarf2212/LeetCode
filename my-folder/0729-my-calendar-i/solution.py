class MyCalendar:

    # [10, 20)
    # [15, 25)

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:

        if len(self.intervals) == 0:
            self.intervals.append([start, end])
            return True

        left = 0
        right = len(self.intervals)
        while left < right:
            mid = (left+right) // 2

            midStart, midEnd = self.intervals[mid]

            if end <= midStart:
                right = mid
            
            elif start >= midEnd:
                left = mid + 1
            
            else:
                return False
        
        self.intervals = self.intervals[:left] + [[start, end]] + self.intervals[left:]
        
        return True
            

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
