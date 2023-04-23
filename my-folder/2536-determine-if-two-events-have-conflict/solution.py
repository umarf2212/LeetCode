class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        class Event:
            def __init__(self, event):
                self.start = list(map(int, event[0].split(":")))
                self.end = list(map(int, event[1].split(":")))
        
        event1 = Event(event1)
        event2 = Event(event2)

        
        if event1.start[0] < event2.start[0]:
            sooner = event1
            later = event2
        
        elif event1.start[0] == event2.start[0] and event1.start[1] <= event2.start[1]:
            sooner = event1
            later = event2
        else:
            sooner = event2
            later = event1
        
        # overlap happens b/w sooner's end and later's start

        # print(sooner.start, sooner.end)
        # print(later.start, later.end)

        if sooner.end[0] > later.start[0]:
            return True
        
        elif sooner.end[0] == later.start[0]:
            if later.start[1] <= sooner.end[1]:
                return True
        
        return False
