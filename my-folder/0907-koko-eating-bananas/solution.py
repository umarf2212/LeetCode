class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # If she only had 1h, she would want to eat all the bananas at once
        # = sum(piles)

        # If she had one pile per hour, max she could eat would be
        # = max(piles)

        # DRY RUN
        # 3 6 7 11
        # max = 11 = lo, sum = 27 = hi
        # mid = 19

        # 11, 18 = 14
        # 11, 13 = 12
        # 11, 11 = 11

        def canEatBananas(piles, h, k):
            # k = max bananas koko chooses to eat per hour
            # so ultimately what we find is how many hours it takes her to 
            # eat the remaining bananas

            hourCount = 0
            for i in range(len(piles)):
                # Now we calculate how many hours it takes koko to finish all the piles
                # If less number of bananas than her speed, she takes one hour.
                # If more bananas than her speed, she takes more than an hour
                # so we can calc this just by dividing no. of bananas in current pile
                # with her speed.
                
                for bananas in piles:
                    # if bananas < speed, let's say 3 < 14, she takes 1 hour
                    # => means 3//14 + 1 = 1

                    # if bananas == speed, 14 == 14
                    # => 14//14 + 1 = 2 which is incorrect as she can eat all at once
                    #    so we offset it by forcing 1 banana for next hour
                    # => (14-1)//14 + 1 : one banana goes into the next hour (+1)

                    # if bananas > speed, 26 > 14
                    # 26//14 + 1 = 2 : takes 2 hours (14+13) 
                    # since this math doesn't add up as + 1 is extra
                    # (26-1)//14 + 1 = 2 hours (14 + 12)

                    for bananas in piles:
                        hourCount += (bananas-1)//k + 1
                    
                    if hourCount > h:
                        return False
                    return True

        lo = 1
        hi = max(piles)
        while lo <= hi:
            mid = (lo+hi)//2

            if canEatBananas(piles, h, mid):
                hi = mid-1
            else:
                lo = mid+1
        
        return lo
