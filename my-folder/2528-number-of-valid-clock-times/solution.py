class Solution:
    def countTime(self, time: str) -> int:
        
        # ? -> 0
        # 0, 1, 2 => 3 possibilities

        # ? -> 1
        # 0, 1 => 10 * 2 => 20
        # 2    => 4 =>
        # = 24 possibilities

        # ? -> 3
        # [0,5] => 6

        # ? -> 4
        # [0,9] => 10

        ans = 1

        if time[0] == '?' and time[1] == '?':
            ans *= 24
        
        elif time[0] == '?':

            if int(time[1]) <= 3:
                ans *= 3
            else:
                ans *= 2
        
        elif time[1] == '?':
            if time[0] == '2':
                ans *= 4
            else:
                ans *= 10
        
        if time[3] == '?':
            ans *= 6
        
        if time[4] == '?':
            ans *= 10
        
        return ans

