class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        # 1 <-> 2 <-> 3 <-> 4

        # n-1 % 5
        # 3 % 5 = 3


        # Let's say one complete cycle is the pillow coming back to 1
        # i.e. n-1 passes to n'th person, and n-1 passes back to 1
        # Total passes in 1 cycle = 2 * (n-1)

        # Now, we simple do time = time % cycle to bring time within the range of 
        # the cycles.
        # Now if time < n: return time + 1
        #  if time > n: return n - (time - (n-1))

        cycle = (2 * (n-1))

        if cycle == 0:
            return 1

        time = time % cycle
        print(time, cycle)

        # 1 <-> 2 <-> 3 <-> 4
        # in 1 s, pillow is passed from 1 to 2, so 2 has it: time+1
        # in 6 s, pillow is passed to 4 in 3s, then another 3s back to 1
        # in 5 s, pillow is passed to 4 in 3s (n-1), 
        # then to 2 in 2s: n - (time-(n-1))

        if time < n:
            return time + 1
        else:
            return n - (time-(n-1))


